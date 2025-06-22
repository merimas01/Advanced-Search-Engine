import math
import torch
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
from sqlmodel import Session
from app.models.generated_models import Product, ProductBrand, ProductColor, ProductDepartment, ProductLabel, SubCategory
from app.db.database import get_db, SessionLocal
from app.schemas.schemas import ProductOut

# Initialize router
router = APIRouter()

# Global variables
model = None
embeddings = None
products_metadata = []  # Holds [{"id": int, "caption": string}]

# Step 1: Load ProductID and captions
def load_products_from_db(db: Session):
    records = (
        db.query(
            Product.ProductID,
            Product.ProductName,
            Product.ProductCaption,
            ProductBrand.BrandName,
            ProductColor.ColorName,
            ProductDepartment.DepartmentName,
            ProductLabel.LabelName,
            SubCategory.SubCategoryName,
        )
        .join(ProductBrand, Product.ProductBrandID == ProductBrand.ProductBrandID)
        .join(ProductColor, Product.ProductColorID == ProductColor.ProductColorID)
        .join(ProductDepartment, Product.ProductDepartmentID == ProductDepartment.ProductDepartmentID)
        .join(ProductLabel, Product.ProductLabelID == ProductLabel.ProductLabelID)
        .join(SubCategory, Product.SubCategoryID == SubCategory.SubCategoryID)
        .all()
    )

    return [
        {
            "id": row[0],
            "caption": f"{row[6]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[7]}"
        }
        for row in records
    ]

# Step 2: Initialize model and compute embeddings
@router.on_event("startup")
def on_startup():
    global model, embeddings, products_metadata

    db = SessionLocal()
    try:
        products_metadata = load_products_from_db(db)
    finally:
        db.close()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    captions = [item["caption"] for item in products_metadata]
    embeddings = model.encode(captions, convert_to_tensor=True, normalize_embeddings=True)

# Step 3: Define schemas
class SearchRequest(BaseModel):
    query: str
    top_k: int = 20
    page: int = 1
    items_per_page: int = 10

class SearchResult(BaseModel):
    results: list[ProductOut]
    currentPage: int
    itemsPerPage: int
    totalPages: int
    totalCount: int

def paginate(items: list, page: int, page_size: int):
    total_items = len(items)
    total_pages = (total_items + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = start + page_size

    return {
        "items": items[start:end],
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
    }

# Step 4: Semantic search using cosine similarity
@router.post("/semantic-search", response_model=SearchResult)
def semantic_search(request: SearchRequest, db: Session = Depends(get_db)):
    query_embedding = model.encode(request.query, convert_to_tensor=True, normalize_embeddings=True)

    # Compute cosine similarity between query and all product captions
    cosine_scores = util.cos_sim(query_embedding, embeddings)[0]  
    print(cosine_scores)
    
    # Sort by similarity score
    top_results = torch.topk(cosine_scores, k=request.top_k)
    top_indices = top_results.indices.cpu().numpy().tolist()

    matched_ids = [products_metadata[i]["id"] for i in top_indices]

    # Fetch Products by ID
    products = db.query(Product).filter(Product.ProductID.in_(matched_ids)).all()
    id_to_product = {product.ProductID: product for product in products}

    ordered_products = [id_to_product[pid] for pid in matched_ids if pid in id_to_product]

    paginated = paginate(ordered_products, request.page, request.items_per_page)

    return SearchResult(
        results=[ProductOut.model_validate(p) for p in paginated["items"]],
        currentPage=paginated["page"],
        itemsPerPage=paginated["page_size"],
        totalPages=math.ceil(request.top_k / request.items_per_page),
        totalCount=len(ordered_products)
    )
