from sqlalchemy.orm import Session
from utils.file_to_base64 import image_to_base64
from db.database import SessionLocal  # your DB session setup
from models import (
    Category,
    SubCategory,
    ProductBrand,
    ProductColor,
    ProductDepartment,
    ProductImage,
    Product,
    Size,
    ProductSize,
    Users,
    SearchHistory,
)


def seed_all_data():
    session: Session = SessionLocal()

    # Seed Categories
    electronics = Category(CategoryName="Electronics")
    fashion = Category(CategoryName="Fashion")
    session.add_all([electronics, fashion])
    session.flush()

    # Seed SubCategories
    mobiles = SubCategory(
        SubCategoryName="Mobile Phones", CategoryID=electronics.CategoryID
    )
    laptops = SubCategory(SubCategoryName="Laptops", CategoryID=electronics.CategoryID)
    clothing = SubCategory(
        SubCategoryName="Men Clothing", CategoryID=fashion.CategoryID
    )
    headphones = SubCategory(SubCategoryName= "Headphones", CategoryID = electronics.CategoryID)
    session.add_all([mobiles, laptops, headphones, clothing])
    session.flush()

    # Seed Brands
    apple = ProductBrand(BrandName="Apple")
    samsung = ProductBrand(BrandName="Samsung")
    nike = ProductBrand(BrandName="Nike")
    sony = ProductBrand (BrandName="Sony")
    session.add_all([apple, samsung, nike, sony])
    session.flush()

    # Seed Colors
    black = ProductColor(ColorName="Black")
    white = ProductColor(ColorName="White")
    red = ProductColor(ColorName="Red")
    session.add_all([black, white, red])
    session.flush()

    # Seed Departments
    tech = ProductDepartment(DepartmentName="Tech")
    wear = ProductDepartment(DepartmentName="Wearables")
    session.add_all([tech, wear])
    session.flush()

    # Seed Product Image
    image1 = ProductImage(ImageBase64="")
    session.add_all([image1])
    session.flush()

    # Seed Products
    iphone = Product(
        ProductName="iPhone 14",
        ProductCaption="Latest Apple iPhone",
        ProductPrice=999.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
    )

    galaxy = Product(
        ProductName="Galaxy S23",
        ProductCaption="Latest Samsung Galaxy",
        ProductPrice=899.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
    )

    tshirt = Product(
        ProductName="Nike T-Shirt",
        ProductCaption="Comfortable and stylish",
        ProductPrice=29.99,
        ProductBrandID=nike.ProductBrandID,
        ProductColorID=red.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
    )

    macbook = Product(
        ProductName="MacBook Pro 14",
        ProductCaption="Powerful laptop for professionals",
        ProductPrice=1999.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
    )

    samsung_laptop = Product(
        ProductName="Samsung Galaxy Book",
        ProductCaption="Portable and sleek design",
        ProductPrice=1299.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
    )

    nike_jacket = Product(
        ProductName="Nike Windrunner Jacket",
        ProductCaption="Stylish and weather resistant",
        ProductPrice=79.99,
        ProductBrandID=nike.ProductBrandID,
        ProductColorID=red.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
    )

    nike_shoes = Product(
        ProductName="Nike Air Max",
        ProductCaption="High performance sports shoes",
        ProductPrice=149.99,
        ProductBrandID=nike.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
    )

    samsung_earbuds = Product(
        ProductName="Samsung Galaxy Buds",
        ProductCaption="Wireless noise-cancelling earbuds",
        ProductPrice=129.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
    )

    samsung_galaxy_s21 = Product(
        ProductName="Samsung Galaxy S21",
        ProductCaption="Next-generation 5G smartphone",
        ProductPrice=799.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
    )

    apple_iphone_13 = Product(
        ProductName="Apple iPhone 13",
        ProductCaption="The latest iPhone with A15 Bionic Chip",
        ProductPrice=799.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
    )
    
    sonny_wh = Product(
        ProductName="Sony WH-1000XM4",
        ProductCaption="Noise Cancelling Over-Ear Headphones",
        ProductPrice=349.99,
        ProductBrandID=sony.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=headphones.SubCategoryID,
    )
    
    session.add_all(
        [
            iphone,
            galaxy,
            tshirt,
            macbook,
            samsung_laptop,
            nike_jacket,
            nike_shoes,
            samsung_earbuds,
            samsung_galaxy_s21,
            apple_iphone_13,
            sonny_wh
        ]
    )
    session.flush()

    # Seed Sizes
    small = Size(SizeName="S")
    medium = Size(SizeName="M")
    large = Size(SizeName="L")
    session.add_all([small, medium, large])
    session.flush()

    # Seed Product Sizes (many-to-many)
    session.add_all(
        [
            ProductSize(ProductID=iphone.ProductID, SizeID=medium.SizeID),
            ProductSize(ProductID=galaxy.ProductID, SizeID=large.SizeID),
            ProductSize(ProductID=tshirt.ProductID, SizeID=small.SizeID),
            ProductSize(ProductID=tshirt.ProductID, SizeID=medium.SizeID),
            ProductSize(ProductID=nike_jacket.ProductID, SizeID=medium.SizeID),
            ProductSize(ProductID=nike_shoes.ProductID, SizeID=large.SizeID),
        ]
    )

    # Seed Users
    user1 = Users(Name="Alice", Surname="Smith", Username="alice", Password="pass123")
    user2 = Users(Name="Bob", Surname="Jones", Username="bob", Password="pass456")
    session.add_all([user1, user2])
    session.flush()

    # Seed Search History
    session.add_all(
        [
            SearchHistory(UserID=user1.UserID, SearchInput="iPhone"),
            SearchHistory(UserID=user2.UserID, SearchInput="Nike T-Shirt"),
        ]
    )

    session.commit()
    session.close()
    print("✅ All seed data inserted successfully.")


if __name__ == "__main__":
    seed_all_data()
