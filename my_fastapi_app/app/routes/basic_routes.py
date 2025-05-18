import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import desc, func
from sqlalchemy.orm import Session, joinedload
from app.db.database import get_db
from app.models.generated_models import Product, ProductImage, SearchHistory
from app.schemas.schemas import ProductImageCreate, ProductImageOut, ProductOut, SearchHistoryCreate, SearchHistoryOut

router = APIRouter()


# Get all products
@router.get("/products", response_model=List[ProductOut])
def get_products(db: Session = Depends(get_db)):
    products = (
        db.query(Product)
        .options(
            joinedload(Product.SubCategory),
            joinedload(Product.ProductColor),
            joinedload(Product.ProductBrand),
            joinedload(Product.ProductImage),
            joinedload(Product.ProductDepartment),
            joinedload(Product.ProductLabel),
        )
        .all()
    )
    return products


# Get product by ID
@router.get("/products/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = (
        db.query(Product)
        .options(
            joinedload(Product.SubCategory),
            joinedload(Product.ProductColor),
            joinedload(Product.ProductBrand),
            joinedload(Product.ProductImage),
            joinedload(Product.ProductDepartment),
            joinedload(Product.ProductLabel),
        )
        .filter(Product.ProductID == product_id)
        .first()
    )

    if not product:
        raise HTTPException(status_code=200, detail="Product not found")

    return product


# Delete product by ID
@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.ProductID == product_id).first()

    if not product:
        raise HTTPException(status_code=200, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}


# Get all search_history
@router.get("/searchHistory", response_model=List[SearchHistoryOut])
def get_history(db: Session = Depends(get_db)):
    history = (
        db.query(SearchHistory)
        .options(
            joinedload(SearchHistory.Users),
        )
        .all()
    )
    return history


# Get all search_history by UserID


@router.get("/searchHistory/{user_id}")
def get_search_history_by_userId(
    user_id: int, searchString: str = Query(None), db: Session = Depends(get_db)
):
    subquery = (
        db.query(func.max(SearchHistory.SearchHistoryID).label("latest_id"))
        .filter(SearchHistory.UserID == user_id)
        .group_by(SearchHistory.SearchInput)
    )

    query = (
        db.query(SearchHistory)
        .options(joinedload(SearchHistory.Users))
        .filter(SearchHistory.SearchHistoryID.in_(subquery))
        .filter(func.trim(SearchHistory.SearchInput) != "")
    )

    if searchString:
        query = query.filter(SearchHistory.SearchInput.ilike(f"%{searchString}%"))

    history = query.order_by(desc(SearchHistory.DateCreated)).limit(5).all()

    if not history:
        raise HTTPException(status_code=200, detail="List not found")

    return history


# Delete search_history by ID
@router.delete("/searchHistory/{sh_id}")
def delete_searchHistory(sh_id: int, db: Session = Depends(get_db)):
    sh = db.query(SearchHistory).filter(SearchHistory.SearchHistoryID == sh_id).first()

    if not sh:
        raise HTTPException(status_code=200, detail="Not found")

    db.delete(sh)
    db.commit()

    return {"message": "Object deleted successfully"}


@router.post("/searchHistory")
def create_search_history(item: SearchHistoryCreate, db: Session = Depends(get_db)):
    new_history = SearchHistory(
        SearchInput=item.SearchInput,
        UserID=item.UserID,
    )
    db.add(new_history)
    db.commit()
    db.refresh(new_history)
    return new_history


@router.put("/product-image/{product_image_id}", response_model=ProductImageCreate)
def update_product_image(
    product_image_id: int,
    item: ProductImageCreate,
    db: Session = Depends(get_db)
):
    image = db.query(ProductImage).filter(ProductImage.ProductImageID == product_image_id).first()
    
    if not image:
        raise HTTPException(status_code=404, detail="ProductImage not found")

    image.ImageBase64 = item.ImageBase64

    db.commit()
    db.refresh(image)

    return image