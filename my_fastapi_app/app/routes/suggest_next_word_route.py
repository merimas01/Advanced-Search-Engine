from typing import List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.generated_models import Product, ProductBrand, ProductColor, ProductLabel, SubCategory
import os

router = APIRouter()
client = OpenAI(api_key=os.getenv("API_KEY"))

# Request model
class SuggestRequest(BaseModel):
    prompt: str
    top_k: int = 5

# Response model
class Suggestion(BaseModel):
    suggestion: str
    rank: int

class SuggestResponse(BaseModel):
    prompt: str
    suggestions: List[Suggestion]

def load_data_from_db(db: Session):
    return (
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

@router.post("/gpt4-suggestions", response_model=SuggestResponse)
def get_gpt4_suggestions(request: SuggestRequest, db: Session = Depends(get_db)):
    rows = load_data_from_db(db)
    if not rows:
        raise HTTPException(status_code=404, detail="No product data found.")

    # Build custom corpus
    corpus = [
        f"{row[0]} {row[1]} {row[2]} {row[4]}"
        for row in rows if all(row)
    ]

    # Construct GPT-4 prompt
    full_prompt = f"""
You are a helpful language model.

Given the following product-related phrases:
{corpus}

Based on these, suggest the {request.top_k} most likely **next words** after the word: \"{request.prompt}\"

Respond with only the {request.top_k} most likely next words, separated by commas, no explanation. If no good suggestions exist, respond with nothing.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=25,
            temperature=0.3
        )
        text = response.choices[0].message.content.strip()
        words = [word.strip() for word in text.split(",") if word.strip()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")

    if not words:
        return SuggestResponse(prompt=request.prompt, suggestions=[])

    return SuggestResponse(
        prompt=request.prompt,
        suggestions=[Suggestion(suggestion=word, rank=i+1) for i, word in enumerate(words)]
    )
