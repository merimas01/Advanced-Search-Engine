from collections import Counter, defaultdict
from typing import List

import torch
from fastapi import APIRouter, Depends, HTTPException
from nltk.util import ngrams
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.generated_models import Product, ProductBrand, ProductColor, ProductLabel, SubCategory

router = APIRouter()

# Load GPT-2 model and tokenizer once
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# Helper to score a candidate using GPT-2
def score_completion(prompt: str, candidate: str) -> float:
    input_text = f"{prompt} {candidate}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    return outputs.loss.item()


# Request and Response Schemas
class SuggestRequest(BaseModel):
    prompt: str
    top_k: int = 5


class Suggestion(BaseModel):
    suggestion: str
    gpt2_loss: float


class SuggestResponse(BaseModel):
    prompt: str
    suggestions: List[Suggestion]


@router.post("/gpt2-suggestions", response_model=SuggestResponse)
def get_gpt2_suggestions(request: SuggestRequest, db: Session = Depends(get_db)):
    # Step 1: Fetch product data
    rows = (
        db.query(
            Product.ProductName,
            ProductBrand.BrandName,
            ProductColor.ColorName,
            ProductLabel.LabelName,
            SubCategory.SubCategoryName
        )
        .join(ProductBrand, Product.ProductBrandID == ProductBrand.ProductBrandID, isouter=True)
        .join(ProductColor, Product.ProductColorID == ProductColor.ProductColorID, isouter=True)
        .join(ProductLabel, Product.ProductLabelID == ProductLabel.ProductLabelID, isouter=True)
        .join(SubCategory, Product.SubCategoryID == SubCategory.SubCategoryID, isouter=True)
        .all()
    )

    if not rows:
        raise HTTPException(status_code=404, detail="No product data found.")

    # Step 2: Build corpus and n-gram index
    corpus = [
        f"{row[3]} {row[0]} {row[1]} {row[2]} {row[4]}"
        for row in rows
        if all(row)
    ]
    tokens = " ".join(corpus).lower().replace(".", "").split()
    bigrams = list(ngrams(tokens, 2))
    bigram_freq = Counter(bigrams)

    next_word_dict = defaultdict(list)
    for (w1, w2), freq in bigram_freq.items():
        next_word_dict[w1].append((w2, freq))

    # Step 3: Get last word from prompt
    last_word = request.prompt.strip().lower().split()[-1]
    candidates = sorted(next_word_dict.get(last_word, []), key=lambda x: -x[1])
    candidate_words = [word for word, _ in candidates[:request.top_k]]

    if not candidate_words:
        return SuggestResponse(prompt=request.prompt, suggestions=[])

    # Step 4: Rank candidates using GPT-2 loss
    scored = [
        Suggestion(suggestion=word, gpt2_loss=score_completion(request.prompt, word))
        for word in candidate_words
    ]
    scored.sort(key=lambda x: x.gpt2_loss)

    return SuggestResponse(prompt=request.prompt, suggestions=scored)
