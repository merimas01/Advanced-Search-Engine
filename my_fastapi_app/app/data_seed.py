from sqlalchemy.orm import Session
from db.database import SessionLocal
from models import (
    Category,
    SubCategory,
    ProductBrand,
    ProductColor,
    ProductDepartment,
    ProductImage,
    ProductLabel,
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
    headphones = SubCategory(
        SubCategoryName="Headphones", CategoryID=electronics.CategoryID
    )
    tv = SubCategory(SubCategoryName="TVs", CategoryID=electronics.CategoryID)
    wearables = SubCategory(
        SubCategoryName="Wearables", CategoryID=electronics.CategoryID
    )
    audio = SubCategory(SubCategoryName="Audio", CategoryID=electronics.CategoryID)
    session.add_all([mobiles, laptops, headphones, clothing, tv, wearables, audio])
    session.flush()

    # Seed Brands
    apple = ProductBrand(BrandName="Apple")
    samsung = ProductBrand(BrandName="Samsung")
    nike = ProductBrand(BrandName="Nike")
    sony = ProductBrand(BrandName="Sony")
    xiaomi = ProductBrand(BrandName="Xiaomi")
    adidas = ProductBrand(BrandName="Adidas")
    hp = ProductBrand(BrandName="HP")
    google = ProductBrand(BrandName="Google")
    puma = ProductBrand(BrandName="Puma")
    lg = ProductBrand(BrandName="LG")
    fitbit = ProductBrand(BrandName="FitBit")
    bose = ProductBrand(BrandName="Bose")
    lenovo = ProductBrand(BrandName="Lenovo")
    dell = ProductBrand(BrandName="Dell")
    session.add_all(
        [
            apple,
            samsung,
            nike,
            sony,
            xiaomi,
            adidas,
            hp,
            google,
            puma,
            lg,
            fitbit,
            bose,
            lenovo,
            dell,
        ]
    )
    session.flush()

    # Seed Colors
    black = ProductColor(ColorName="Black")
    white = ProductColor(ColorName="White")
    red = ProductColor(ColorName="Red")
    grey = ProductColor(ColorName="Grey")
    green = ProductColor(ColorName="Green")
    silver = ProductColor(ColorName="Silver")
    pink = ProductColor(ColorName="Pink")
    blue = ProductColor(ColorName="Blue")
    session.add_all([black, white, red, grey, green, silver, pink, blue])
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

    # Seed Product Labels

    standard = ProductLabel(LabelName="Standard")
    sale = ProductLabel(LabelName="Sale")
    new = ProductLabel(LabelName="New")
    super_price = ProductLabel(LabelName="Super price")
    session.add_all([standard, sale, new, super_price])
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
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
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
        NewPrice=1880.99,
        ProductLabelID=super_price.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
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
        NewPrice=40.99,
        ProductLabelID=sale.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
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
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    xiaomi_phone = Product(
        ProductName="Xiaomi Redmi Note 12",
        ProductCaption="Affordable power with stunning display",
        ProductPrice=299.99,
        ProductBrandID=xiaomi.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    sony_tv = Product(
        ProductName='Sony Bravia 55" 4K TV',
        ProductCaption="Crystal-clear visuals and smart features",
        ProductPrice=699.99,
        ProductBrandID=sony.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=tv.SubCategoryID,
        NewPrice=649.99,
        ProductLabelID=super_price.ProductLabelID,
    )

    adidas_shoes = Product(
        ProductName="Adidas Ultraboost",
        ProductCaption="Maximum comfort for running",
        ProductPrice=159.99,
        ProductBrandID=adidas.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    hp_laptop = Product(
        ProductName="HP Pavilion 15",
        ProductCaption="Reliable performance for everyday tasks",
        ProductPrice=749.99,
        ProductBrandID=hp.ProductBrandID,
        ProductColorID=grey.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=699.99,
        ProductLabelID=sale.ProductLabelID,
    )

    apple_watch = Product(
        ProductName="Apple Watch Series 8",
        ProductCaption="Advanced health tracking and style",
        ProductPrice=399.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=wearables.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    dell_xps = Product(
        ProductName="Dell XPS 13",
        ProductCaption="Compact and powerful ultrabook",
        ProductPrice=1399.99,
        ProductBrandID=dell.ProductBrandID,
        ProductColorID=silver.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    lenovo_legion = Product(
        ProductName="Lenovo Legion 5",
        ProductCaption="Gaming laptop with high refresh rate display",
        ProductPrice=1149.99,
        ProductBrandID=lenovo.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=999.99,
        ProductLabelID=super_price.ProductLabelID,
    )

    fitbit_versa = Product(
        ProductName="Fitbit Versa 3",
        ProductCaption="Health & fitness smartwatch",
        ProductPrice=229.99,
        ProductBrandID=fitbit.ProductBrandID,
        ProductColorID=pink.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=wearables.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    lg_oled_tv = Product(
        ProductName='LG OLED C1 65"',
        ProductCaption="Stunning OLED visuals with Dolby Vision",
        ProductPrice=1799.99,
        ProductBrandID=lg.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=tv.SubCategoryID,
        NewPrice=1599.99,
        ProductLabelID=sale.ProductLabelID,
    )

    adidas_hoodie = Product(
        ProductName="Adidas Essentials Hoodie",
        ProductCaption="Warm and comfortable hoodie",
        ProductPrice=49.99,
        ProductBrandID=adidas.ProductBrandID,
        ProductColorID=grey.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    puma_running_shoes = Product(
        ProductName="Puma Velocity Nitro",
        ProductCaption="Responsive running shoes for daily runs",
        ProductPrice=119.99,
        ProductBrandID=puma.ProductBrandID,
        ProductColorID=blue.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    sony_soundbar = Product(
        ProductName="Sony HT-G700 Soundbar",
        ProductCaption="Immersive cinematic audio",
        ProductPrice=499.99,
        ProductBrandID=sony.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=audio.SubCategoryID,
        NewPrice=449.99,
        ProductLabelID=super_price.ProductLabelID,
    )

    bose_qc45 = Product(
        ProductName="Bose QuietComfort 45",
        ProductCaption="Top-tier noise-cancelling headphones",
        ProductPrice=329.99,
        ProductBrandID=bose.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=headphones.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    apple_airpods_pro = Product(
        ProductName="Apple AirPods Pro 2",
        ProductCaption="Personalized Spatial Audio & ANC",
        ProductPrice=249.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=headphones.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    google_pixel = Product(
        ProductName="Google Pixel 7",
        ProductCaption="Pure Android experience and great camera",
        ProductPrice=649.99,
        ProductBrandID=google.ProductBrandID,
        ProductColorID=green.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image1.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=599.99,
        ProductLabelID=sale.ProductLabelID,
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
            sonny_wh,
            xiaomi_phone,
            sony_tv,
            adidas_shoes,
            hp_laptop,
            apple_watch,
            dell_xps,
            lenovo_legion,
            fitbit_versa,
            lg_oled_tv,
            adidas_hoodie,
            puma_running_shoes,
            sony_soundbar,
            bose_qc45,
            apple_airpods_pro,
            google_pixel,
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
