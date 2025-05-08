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
    ImagePath: Optional[str]
    ImageBase64: Optional[bytes]

    class Config:
        from_attributes = True

class ProductImageCreate(BaseModel):
    ImageBase64 : Optional[bytes]
      
    class Config:
        from_attributes = True

class ProductDepartmentOut(BaseModel):
    ProductDepartmentID: int
    DepartmentName: str

    class Config:
        from_attributes = True


class ProductLabelOut(BaseModel):
    ProductLabelID: int
    LabelName: str

    class Config:
        from_attributes = True


class ProductOut(BaseModel):
    ProductID: int
    ProductName: str
    ProductCaption: str
    ProductPrice: Decimal
    NewPrice: Optional[Decimal] = None
    DateCreated: datetime

    SubCategory: SubCategoryOut
    ProductColor: ProductColorOut
    ProductBrand: ProductBrandOut
    ProductImage: ProductImageOut
    ProductDepartment: ProductDepartmentOut
    ProductLabel: Optional[ProductLabelOut] = None
    ProductSize: List["ProductSizeOut"]

    class Config:
        from_attributes = True


class SizeOut(BaseModel):
    SizeID: int
    SizeName: str

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
    Surname: str
    Username: str
    Password: str

    class Config:
        from_attributes = True


class SearchHistoryOut(BaseModel):
    SearchHistoryID: int
    SearchInput: str
    DateCreated: datetime
    Users: UsersOut

    class Config:
        from_attributes = True


class SearchHistoryCreate(BaseModel):
    SearchInput: str
    UserID: int
