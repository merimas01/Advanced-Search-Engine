from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from sqlmodel import Session
from app.models.generated_models import Product, ProductBrand, ProductColor, ProductDepartment, ProductLabel, SubCategory
from app.db.database import get_db, SessionLocal
from app.schemas.schemas import ProductOut

# Initialize router
router = APIRouter()

# Global variables
model = None
index = None
products_metadata = []  # Holds [{"id": ProductID, "caption": ProductCaption}]


# Step 1: Load ProductID and other objects from database

def load_products_from_db(db: Session):
    records = (
        db.query(
            Product.ProductID,
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
            "caption": f"{row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]}"
        }
        for row in records
    ]
# Step 2: Initialize model and FAISS index at startup
@router.on_event("startup")
def on_startup():
    global model, index, products_metadata

    db = SessionLocal()
    try:
        products_metadata = load_products_from_db(db)
    finally:
        db.close()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    captions = [item["caption"] for item in products_metadata]
    embeddings = model.encode(captions)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))


# Step 3: Define request and response schemas
class SearchRequest(BaseModel):
    query: str
    top_k: int = 2  # Default: return top 2 results
    page: int = 1
    items_per_page: int = 2


class SearchResult(BaseModel):
    results: list[ProductOut]
    currentPage: int
    itemsPerPage: int
    totalPages: int
    totalCount: int


# Helper function to paginate items
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


# Step 4: Define semantic search route
@router.post("/semantic-search", response_model=SearchResult)
def semantic_search(request: SearchRequest, db: Session = Depends(get_db)):
    query_embedding = model.encode([request.query])
    distances, indices = index.search(np.array(query_embedding), k=request.top_k)

    matched = [products_metadata[idx] for idx in indices[0]]
    matched_ids = [item["id"] for item in matched]

    # Fetch Products from database by matched IDs
    products = db.query(Product).filter(Product.ProductID.in_(matched_ids)).all()

    # Reorder products to match search order
    id_to_product = {product.ProductID: product for product in products}
    ordered_products = [
        id_to_product[pid] for pid in matched_ids if pid in id_to_product
    ]

    paginated = paginate(ordered_products, request.page, request.items_per_page)

    return SearchResult(
        results=[ProductOut.model_validate(p) for p in paginated["items"]],
        currentPage=paginated["page"],
        itemsPerPage=paginated["page_size"],
        totalPages=paginated["total_pages"],
        totalCount=paginated["total_items"],
    )
