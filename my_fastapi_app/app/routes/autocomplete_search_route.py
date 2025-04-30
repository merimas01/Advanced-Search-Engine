from fastapi import APIRouter, Depends
from pydantic import BaseModel
from collections import Counter
from nltk.util import ngrams
from sqlalchemy.orm import Session

from app.db.database import get_db  
from app.models.generated_models import Product  

router = APIRouter()


class SuggestNextWordsRequest(BaseModel):
    context: list[str]


class SuggestNextWordsResponse(BaseModel):
    suggestions: list[str]


@router.post("/suggest-next-words", response_model=SuggestNextWordsResponse)
def suggest_next_words(request: SuggestNextWordsRequest, db: Session = Depends(get_db)):
    # Step 1: Load all sentences
    sentences = db.query(Product.ProductCaption).all()
    corpus_list = [row[0] for row in sentences if row[0]]  # protect against None

    # Step 2: Filter corpus to only sentences containing the context words
    filtered_corpus_list = [
        text for text in corpus_list
        if all(word.lower() in text.lower() for word in request.context)
    ]

    if not filtered_corpus_list:
        return SuggestNextWordsResponse(suggestions=[])

    # Step 3: Join filtered sentences into one large text
    corpus = " ".join(filtered_corpus_list)

    # Step 4: Tokenize
    words = corpus.split()

    # Step 5: Create bigrams and trigrams
    bigrams = list(ngrams(words, 2))
    trigrams = list(ngrams(words, 3))

    # Step 6: Count n-grams
    bigram_counts = Counter(bigrams)
    trigram_counts = Counter(trigrams)

    # Step 7: Prepare context tuple
    context = tuple(request.context)

    # Step 8: Find candidates
    single_word_candidates = [
        bigram[1] for bigram in bigram_counts if bigram[0] == context[-1]
    ]
    single_word_freq = Counter(single_word_candidates)

    two_word_candidates = [
        f"{trigram[1]} {trigram[2]}"
        for trigram in trigram_counts
        if trigram[0] == context[-1]
    ]
    two_word_freq = Counter(two_word_candidates)

    # Step 9: Collect top N suggestions
    top_n = 5
    single_word_suggestions = [word for word, _ in single_word_freq.most_common(top_n)]
    two_word_suggestions = [phrase for phrase, _ in two_word_freq.most_common(top_n)]

    suggestions = single_word_suggestions + two_word_suggestions

    return SuggestNextWordsResponse(suggestions=suggestions)
