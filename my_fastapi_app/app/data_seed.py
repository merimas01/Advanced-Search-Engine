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

    image_mobile = ProductImage(
        ImagePath="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9.jpeg",
        ImageBase64=None,
    )
    image_laptop = ProductImage(
        ImagePath="https://images.unsplash.com/photo-1517336714731-489689fd1ca8.jpeg",
        ImageBase64=None,
    )
    image_tv = ProductImage(
        ImagePath="https://hackaday.com/wp-content/uploads/2023/05/telly-startup-featured.jpg",
        ImageBase64=None,
    )
    image_shoes = ProductImage(
        ImagePath="https://img.freepik.com/free-photo/fashion-shoes-sneakers_1203-7529.jpg?semt=ais_hybrid&w=740.avif",
        ImageBase64=None,
    )
    image_jacket = ProductImage(
        ImagePath="https://images.teemill.com/dpsuued0awwmlyoqbukwvfiudddvh8hgxbab35h8yj4xnsmi.png.jpg?w=1080&h=1080&v=2.jpeg",
        ImageBase64=None,
    )
    image_shirt = ProductImage(
        ImagePath="https://img.kwcdn.com/product/fancy/dae396d4-dc2f-48f5-a3ca-8ded5944726b.jpg?imageMogr2/auto-orient%7CimageView2/2/w/800/q/70/format/webp.webp",
        ImageBase64=None,
    )
    image_headphones = ProductImage(
        ImagePath="https://unblast.com/wp-content/uploads/2020/07/Headphone-Mockup-1.jpg",
        ImageBase64=None,
    )
    session.add_all(
        [
            image_mobile,
            image_laptop,
            image_tv,
            image_shoes,
            image_jacket,
            image_shirt,
            image_headphones,
        ]
    )
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
        ProductCaption="The latest flagship smartphone from Apple, featuring a stunning display and powerful A15 Bionic chip.",
        ProductPrice=999.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    galaxy = Product(
        ProductName="Galaxy S23",
        ProductCaption="Samsung's cutting-edge smartphone with a gorgeous screen, advanced camera features, and powerful performance.",
        ProductPrice=899.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    tshirt = Product(
        ProductName="Nike T-Shirt",
        ProductCaption="A comfortable and stylish T-shirt made with high-quality materials, perfect for any casual outing.",
        ProductPrice=29.99,
        ProductBrandID=nike.ProductBrandID,
        ProductColorID=red.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_shirt.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    macbook = Product(
        ProductName="MacBook Pro 14",
        ProductCaption="Apple's powerhouse laptop designed for professionals, featuring the M1 Pro chip and a stunning Retina display.",
        ProductPrice=1999.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_laptop.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=1880.99,
        ProductLabelID=super_price.ProductLabelID,
    )

    samsung_laptop = Product(
        ProductName="Samsung Galaxy Book",
        ProductCaption="A sleek and portable laptop with long-lasting battery life, perfect for work and play.",
        ProductPrice=1299.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_laptop.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    nike_jacket = Product(
        ProductName="Nike Windrunner Jacket",
        ProductCaption="A stylish and weather-resistant jacket, perfect for outdoor activities or casual wear in any season.",
        ProductPrice=79.99,
        ProductBrandID=nike.ProductBrandID,
        ProductColorID=red.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_jacket.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=40.99,
        ProductLabelID=sale.ProductLabelID,
    )

    nike_shoes = Product(
        ProductName="Nike Air Max",
        ProductCaption="High-performance running shoes with Air-Sole cushioning and a sleek design for comfort and support.",
        ProductPrice=149.99,
        ProductBrandID=nike.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_shoes.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    samsung_earbuds = Product(
        ProductName="Samsung Galaxy Buds",
        ProductCaption="Wireless, noise-cancelling earbuds with exceptional sound quality, perfect for music lovers and commuters.",
        ProductPrice=129.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    samsung_galaxy_s21 = Product(
        ProductName="Samsung Galaxy S21",
        ProductCaption="Next-generation 5G smartphone with an all-day battery, ultra-responsive camera, and stunning display.",
        ProductPrice=799.99,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    apple_iphone_13 = Product(
        ProductName="Apple iPhone 13",
        ProductCaption="The iPhone 13 features an A15 Bionic chip, 5G capabilities, and an ultra-wide camera for amazing photos and videos.",
        ProductPrice=799.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    sonny_wh = Product(
        ProductName="Sony WH-1000XM4",
        ProductCaption="Noise-cancelling over-ear headphones offering premium sound quality and superior comfort for long listening sessions.",
        ProductPrice=349.99,
        ProductBrandID=sony.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=headphones.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    xiaomi_phone = Product(
        ProductName="Xiaomi Redmi Note 12",
        ProductCaption="An affordable smartphone with a stunning display and powerful performance, ideal for budget-conscious buyers.",
        ProductPrice=299.99,
        ProductBrandID=xiaomi.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    sony_tv = Product(
        ProductName='Sony Bravia 55" 4K TV',
        ProductCaption="A 55-inch smart 4K TV with crisp visuals, immersive sound, and a variety of smart features for a cinematic experience.",
        ProductPrice=699.99,
        ProductBrandID=sony.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_tv.ProductImageID,
        SubCategoryID=tv.SubCategoryID,
        NewPrice=649.99,
        ProductLabelID=super_price.ProductLabelID,
    )

    adidas_shoes = Product(
        ProductName="Adidas Ultraboost",
        ProductCaption="High-performance running shoes with incredible comfort, cushioning, and a sleek modern design.",
        ProductPrice=159.99,
        ProductBrandID=adidas.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_shoes.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    hp_laptop = Product(
        ProductName="HP Pavilion 15",
        ProductCaption="A reliable laptop perfect for daily use, offering excellent performance and value for money.",
        ProductPrice=749.99,
        ProductBrandID=hp.ProductBrandID,
        ProductColorID=grey.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_laptop.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=699.99,
        ProductLabelID=sale.ProductLabelID,
    )

    apple_watch = Product(
        ProductName="Apple Watch Series 8",
        ProductCaption="The ultimate smartwatch for fitness tracking, notifications, and health monitoring with a sleek design.",
        ProductPrice=399.99,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=wearables.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    dell_xps = Product(
        ProductName="Dell XPS 13",
        ProductCaption="Compact and powerful ultrabook with a stunning display and premium build quality.",
        ProductPrice=1399.99,
        ProductBrandID=dell.ProductBrandID,
        ProductColorID=silver.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_laptop.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    lenovo_legion = Product(
        ProductName="Lenovo Legion 5",
        ProductCaption="A gaming laptop with a high refresh rate display, powerful GPU, and exceptional performance for gaming enthusiasts.",
        ProductPrice=1149.99,
        ProductBrandID=lenovo.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_laptop.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=999.99,
        ProductLabelID=super_price.ProductLabelID,
    )

    fitbit_versa = Product(
        ProductName="Fitbit Versa 3",
        ProductCaption="A health & fitness smartwatch designed to help you stay active, monitor sleep, and track daily activities.",
        ProductPrice=229.99,
        ProductBrandID=fitbit.ProductBrandID,
        ProductColorID=pink.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=wearables.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    lg_oled_tv = Product(
        ProductName='LG OLED C1 65"',
        ProductCaption="A 65-inch OLED TV with exceptional color accuracy, deep blacks, and Dolby Vision for an immersive viewing experience.",
        ProductPrice=1799.99,
        ProductBrandID=lg.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_tv.ProductImageID,
        SubCategoryID=tv.SubCategoryID,
        NewPrice=1599.99,
        ProductLabelID=sale.ProductLabelID,
    )

    adidas_hoodie = Product(
        ProductName="Adidas Essentials Hoodie",
        ProductCaption="A warm and comfortable hoodie designed for everyday wear, with a cozy fit and classic style.",
        ProductPrice=49.99,
        ProductBrandID=adidas.ProductBrandID,
        ProductColorID=grey.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_jacket.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=standard.ProductLabelID,
    )

    puma_running_shoes = Product(
        ProductName="Puma Velocity Nitro",
        ProductCaption="Responsive and lightweight running shoes, designed for daily runs and maximum comfort.",
        ProductPrice=119.99,
        ProductBrandID=puma.ProductBrandID,
        ProductColorID=blue.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_shoes.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=None,
        ProductLabelID=new.ProductLabelID,
    )

    sony_soundbar = Product(
        ProductName="Sony HT-G700 Soundbar",
        ProductCaption="An immersive cinematic audio experience with clear sound and deep bass to complement your home theater.",
        ProductPrice=499.99,
        ProductBrandID=sony.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=audio.SubCategoryID,
        NewPrice=449.99,
        ProductLabelID=sale.ProductLabelID,
    )

    bose_qc45 = Product(
        ProductName="Bose QuietComfort 45",
        ProductCaption="High-fidelity noise-canceling headphones for immersive sound and comfort.",
        ProductPrice=329.00,
        ProductBrandID=bose.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=audio.SubCategoryID,
        NewPrice=299.00,
        ProductLabelID=sale.ProductLabelID,
    )

    apple_airpods_pro = Product(
        ProductName="Apple AirPods Pro",
        ProductCaption="Active noise cancellation and adaptive EQ for a premium wireless audio experience.",
        ProductPrice=249.00,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=audio.SubCategoryID,
        NewPrice=229.00,
        ProductLabelID=new.ProductLabelID,
    )

    google_pixel = Product(
        ProductName="Google Pixel 7",
        ProductCaption="Google’s flagship phone with an exceptional camera and pure Android experience.",
        ProductPrice=599.00,
        ProductBrandID=google.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=549.00,
        ProductLabelID=sale.ProductLabelID,
    )

    google_pixel_8 = Product(
        ProductName="Google Pixel 8",
        ProductCaption="The latest Google Pixel with advanced AI features and an upgraded camera system.",
        ProductPrice=699.00,
        ProductBrandID=google.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=649.00,
        ProductLabelID=new.ProductLabelID,
    )

    samsung_galaxy_z_fold = Product(
        ProductName="Samsung Galaxy Z Fold",
        ProductCaption="Futuristic foldable smartphone with a massive display and multitasking capabilities.",
        ProductPrice=1799.00,
        ProductBrandID=samsung.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_mobile.ProductImageID,
        SubCategoryID=mobiles.SubCategoryID,
        NewPrice=1699.00,
        ProductLabelID=new.ProductLabelID,
    )

    macbook_air_m2 = Product(
        ProductName="MacBook Air M2",
        ProductCaption="Supercharged by the Apple M2 chip, ultra-light, and efficient for everyday productivity.",
        ProductPrice=1199.00,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=silver.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_laptop.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=1099.00,
        ProductLabelID=sale.ProductLabelID,
    )

    sony_wh1000xm5 = Product(
        ProductName="Sony WH-1000XM5",
        ProductCaption="Industry-leading noise cancellation headphones with exceptional sound clarity.",
        ProductPrice=399.00,
        ProductBrandID=sony.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=audio.SubCategoryID,
        NewPrice=379.00,
        ProductLabelID=sale.ProductLabelID,
    )

    nike_air_max_2023 = Product(
        ProductName="Nike Air Max 2023",
        ProductCaption="Comfortable and stylish performance sneakers for everyday wear and workouts.",
        ProductPrice=149.00,
        ProductBrandID=nike.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_shoes.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=129.00,
        ProductLabelID=sale.ProductLabelID,
    )

    adidas_superstar = Product(
        ProductName="Adidas Superstar",
        ProductCaption="Iconic sneakers with classic shell toe design and premium comfort.",
        ProductPrice=99.00,
        ProductBrandID=adidas.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=wear.ProductDepartmentID,
        ProductImageID=image_shoes.ProductImageID,
        SubCategoryID=clothing.SubCategoryID,
        NewPrice=89.00,
        ProductLabelID=sale.ProductLabelID,
    )

    hp_spectre_x360 = Product(
        ProductName="HP Spectre x360",
        ProductCaption="Sleek convertible laptop with touch display and top-tier performance.",
        ProductPrice=1399.00,
        ProductBrandID=hp.ProductBrandID,
        ProductColorID=silver.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_laptop.ProductImageID,
        SubCategoryID=laptops.SubCategoryID,
        NewPrice=1299.00,
        ProductLabelID=new.ProductLabelID,
    )

    bose_quietcomfort_45 = Product(
        ProductName="Bose QuietComfort 45",
        ProductCaption="Legendary comfort and premium noise-canceling technology for pure audio enjoyment.",
        ProductPrice=329.00,
        ProductBrandID=bose.ProductBrandID,
        ProductColorID=black.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=audio.SubCategoryID,
        NewPrice=309.00,
        ProductLabelID=sale.ProductLabelID,
    )

    lg_cinebeam_projector = Product(
        ProductName="LG CineBeam Projector",
        ProductCaption="Portable smart projector delivering stunning visuals for home cinema lovers.",
        ProductPrice=999.00,
        ProductBrandID=lg.ProductBrandID,
        ProductColorID=white.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_tv.ProductImageID,
        SubCategoryID=tv.SubCategoryID,
        NewPrice=949.00,
        ProductLabelID=new.ProductLabelID,
    )

    apple_watch_ultra = Product(
        ProductName="Apple Watch Ultra",
        ProductCaption="Rugged and capable smartwatch built for endurance and exploration.",
        ProductPrice=799.00,
        ProductBrandID=apple.ProductBrandID,
        ProductColorID=red.ProductColorID,
        ProductDepartmentID=tech.ProductDepartmentID,
        ProductImageID=image_headphones.ProductImageID,
        SubCategoryID=wearables.SubCategoryID,
        NewPrice=749.00,
        ProductLabelID=new.ProductLabelID,
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
            google_pixel_8,
            samsung_galaxy_z_fold,
            macbook_air_m2,
            sony_wh1000xm5,
            nike_air_max_2023,
            adidas_superstar,
            hp_spectre_x360,
            bose_quietcomfort_45,
            lg_cinebeam_projector,
            apple_watch_ultra,
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
