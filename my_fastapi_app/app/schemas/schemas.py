from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import List, Optional


class SubCategoryOut(BaseModel):
    SubCategoryID: int
    SubCategoryName: str

    class Config:
        from_attributes = True


class ProductColorOut(BaseModel):
    ProductColorID: int
    ColorName: str

    class Config:
        from_attributes = True


class ProductBrandOut(BaseModel):
    ProductBrandID: int
    BrandName: str

    class Config:
        from_attributes = True

class ProductImageOut(BaseModel):
    ProductImageID: int
    ImageBase64: Optional[str]

    class Config:
        from_attributes = True


class ProductDepartmentOut(BaseModel):
    ProductDepartmentID: int
    DepartmentName: str

    class Config:
        from_attributes = True


class ProductOut(BaseModel):
    ProductID: int
    ProductName: str
    ProductCaption: str
    ProductPrice: Decimal
    DateCreated: datetime

    SubCategory: SubCategoryOut
    ProductColor: ProductColorOut
    ProductBrand: ProductBrandOut
    ProductImage: ProductImageOut
    ProductDepartment: ProductDepartmentOut
    ProductSize: List['ProductSizeOut']

    class Config:
        from_attributes = True

       
class SizeOut(BaseModel):
    SizeID:int
    SizeName:str
    
    class Config:
        from_attributes = True


class ProductSizeOut(BaseModel):
    ProductSizeID: int
    
    Available: bool
    Size: SizeOut
    
    class Config:
        from_attributes = True
 
class UsersOut(BaseModel):
    UserID: int
    Name: str
    Surname : str
    Username : str
    Password: str

    class Config:
        from_attributes = True


class SearchHistoryOut(BaseModel):
    SearchHistoryID: int
    SearchInput: str
    DateCreated : datetime
    Users: UsersOut

    class Config:
        from_attributes = True
