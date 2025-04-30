from typing import List, Optional

from sqlalchemy import Boolean, DECIMAL, Column, DateTime, ForeignKey, ForeignKeyConstraint, Identity, Integer, PrimaryKeyConstraint, String, Unicode, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from sqlmodel import SQLModel


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'Category'
    __table_args__ = (
        PrimaryKeyConstraint('CategoryID', name='PK__Category__19093A2B2FA11AB0'),
    )

    CategoryID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    CategoryName: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))

    SubCategory: Mapped[List['SubCategory']] = relationship('SubCategory', back_populates='Category_')


class ProductBrand(Base):
    __tablename__ = 'ProductBrand'
    __table_args__ = (
        PrimaryKeyConstraint('ProductBrandID', name='PK__ProductB__B195942918F532D3'),
    )

    ProductBrandID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    BrandName: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))

    Product: Mapped[List['Product']] = relationship('Product', back_populates='ProductBrand')


class ProductColor(Base):
    __tablename__ = 'ProductColor'
    __table_args__ = (
        PrimaryKeyConstraint('ProductColorID', name='PK__ProductC__C5DB681E618263FE'),
    )

    ProductColorID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    ColorName: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))

    Product: Mapped[List['Product']] = relationship('Product', back_populates='ProductColor')


class ProductDepartment(Base):
    __tablename__ = 'ProductDepartment'
    __table_args__ = (
        PrimaryKeyConstraint('ProductDepartmentID', name='PK__ProductD__DFE96784B2871EA9'),
    )

    ProductDepartmentID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    DepartmentName: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))

    Product: Mapped[List['Product']] = relationship('Product', back_populates='ProductDepartment')


class ProductImage(Base):
    __tablename__ = 'ProductImage'
    __table_args__ = (
        PrimaryKeyConstraint('ProductImageID', name='PK__ProductI__07B2B1D8E2AE328C'),
    )

    ProductImageID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    ImageBase64: Mapped[Optional[str]] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))

    Product: Mapped[List['Product']] = relationship('Product', back_populates='ProductImage')


class Size(Base):
    __tablename__ = 'Size'
    __table_args__ = (
        PrimaryKeyConstraint('SizeID', name='PK__Size__83BD095A8356957D'),
    )

    SizeID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    SizeName: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))

    ProductSize: Mapped[List['ProductSize']] = relationship('ProductSize', back_populates='Size')


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = (
        PrimaryKeyConstraint('UserID', name='PK__Users__1788CCAC4B26C4DD'),
    )

    UserID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    Name: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Surname: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Username: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Password: Mapped[str] = mapped_column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))

    SearchHistory: Mapped[List['SearchHistory']] = relationship('SearchHistory', back_populates='Users')


class SearchHistory(Base):
    __tablename__ = 'SearchHistory'
    __table_args__ = (
        ForeignKeyConstraint(['UserID'], ['Users.UserID'], name='FK__SearchHis__UserI__07C12930'),
        PrimaryKeyConstraint('SearchHistoryID', name='PK__SearchHi__555F7C991720DCE6')
    )

    SearchHistoryID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    SearchInput: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    UserID: Mapped[int] = mapped_column(Integer)
    
    Users: Mapped['Users'] = relationship('Users', back_populates='SearchHistory')


class SubCategory(Base):
    __tablename__ = 'SubCategory'
    __table_args__ = (
        ForeignKeyConstraint(['CategoryID'], ['Category.CategoryID'], name='FK__SubCatego__Categ__46E78A0C'),
        PrimaryKeyConstraint('SubCategoryID', name='PK__SubCateg__26BE5BF9F7AD0B9D')
    )

    SubCategoryID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    SubCategoryName: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))
    CategoryID: Mapped[int] = mapped_column(Integer)

    Category_: Mapped['Category'] = relationship('Category', back_populates='SubCategory')
    Product: Mapped[List['Product']] = relationship('Product', back_populates='SubCategory')


class Product(Base):
    __tablename__ = 'Product'
    __table_args__ = (
        ForeignKeyConstraint(['ProductBrandID'], ['ProductBrand.ProductBrandID'], name='FK__Product__Product__7E37BEF6'),
        ForeignKeyConstraint(['ProductColorID'], ['ProductColor.ProductColorID'], name='FK__Product__Product__7D439ABD'),
        ForeignKeyConstraint(['ProductDepartmentID'], ['ProductDepartment.ProductDepartmentID'], name='FK__Product__Product__7F2BE32F'),
        ForeignKeyConstraint(['ProductImageID'], ['ProductImage.ProductImageID'], name='FK__Product__Product__7C4F7684'),
        ForeignKeyConstraint(['SubCategoryID'], ['SubCategory.SubCategoryID'], name='FK__Product__SubCate__7B5B524B'),
        PrimaryKeyConstraint('ProductID', name='PK__Product__B40CC6EDA3787350')
    )
 
    ProductID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    ProductName: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    ProductCaption: Mapped[str] = mapped_column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    ProductPrice: Mapped[decimal.Decimal] = mapped_column(DECIMAL(8, 2))
    DateCreated: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('(getdate())'))

    ProductBrand: Mapped['ProductBrand'] = relationship('ProductBrand', back_populates='Product')
    ProductColor: Mapped['ProductColor'] = relationship('ProductColor', back_populates='Product')
    ProductDepartment: Mapped['ProductDepartment'] = relationship('ProductDepartment', back_populates='Product')
    ProductImage: Mapped['ProductImage'] = relationship('ProductImage', back_populates='Product')
    SubCategory: Mapped['SubCategory'] = relationship('SubCategory', back_populates='Product')    
    ProductSize: Mapped[List['ProductSize']] = relationship('ProductSize', back_populates='Product_')

    SubCategoryID = Column(Integer, ForeignKey("SubCategory.SubCategoryID"))
    ProductColorID = Column(Integer, ForeignKey("ProductColor.ProductColorID"))
    ProductBrandID = Column(Integer, ForeignKey("ProductBrand.ProductBrandID"))
    ProductImageID = Column(Integer, ForeignKey("ProductImage.ProductImageID"))
    ProductDepartmentID = Column(Integer, ForeignKey("ProductDepartment.ProductDepartmentID"))


class ProductSize(Base):
    __tablename__ = 'ProductSize'
    __table_args__ = (
        ForeignKeyConstraint(['ProductID'], ['Product.ProductID'], name='FK__ProductSi__Produ__02084FDA'),
        ForeignKeyConstraint(['SizeID'], ['Size.SizeID'], name='FK__ProductSi__SizeI__02FC7413'),
        PrimaryKeyConstraint('ProductSizeID', name='PK__ProductS__9DADF571A548B0CF')
    )

    ProductSizeID: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1), primary_key=True)
    ProductID: Mapped[int] = mapped_column(Integer)
    SizeID: Mapped[int] = mapped_column(Integer)
    Available: Mapped[bool] = mapped_column(Boolean, server_default=text('((1))'))

    Product_: Mapped['Product'] = relationship('Product', back_populates='ProductSize')
    Size: Mapped['Size'] = relationship('Size', back_populates='ProductSize')
