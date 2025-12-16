from sqlalchemy.orm import Session

from .database import SessionLocal, Base, engine
from .models import Brand, Category, Product


def run():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    # Brands
    brands = [
        ("Apple", "apple", "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"),
        ("Samsung", "samsung", "https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg"),
        ("Google", "google", "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"),
        ("Dyson", "dyson", None),
        ("Logitech", "logitech", None),
        ("Garmin", "garmin", None),
    ]
    for name, slug, logo in brands:
        if not db.query(Brand).filter_by(slug=slug).first():
            db.add(Brand(name=name, slug=slug, logo_url=logo))

    # Categories
    categories = [
        ("Смартфони", "smartphones"),
        ("Ноутбуки", "laptops"),
        ("Смарт-годинники", "smartwatches"),
        ("Телевізори", "tvs"),
        ("Планшети", "tablets"),
        ("Аксесуари", "accessories"),
    ]
    for name, slug in categories:
        if not db.query(Category).filter_by(slug=slug).first():
            db.add(Category(name=name, slug=slug))

    db.commit()

    # Products demo
    demo_products = [
        {
            "name": "iPhone 15 128GB",
            "slug": "iphone-15-128",
            "price": 799.0,
            "discount_percent": 10,
            "image_url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-1.jpg",
            "short_desc": "OLED, A16 Bionic",
            "description": "iPhone 15 — смартфон із яскравим OLED дисплеєм, камерою з нічним режимом та продуктивним чипом A16 Bionic. Підтримка 5G, MagSafe та довга автономність.\n\nКомплектація: смартфон, кабель USB‑C.",
            "category": "smartphones",
            "brand": "apple",
        },
        {
            "name": "Samsung Galaxy S24",
            "slug": "galaxy-s24",
            "price": 699.0,
            "discount_percent": 0,
            "image_url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-1.jpg",
            "short_desc": "Dynamic AMOLED 2X",
            "description": "Galaxy S24 — флагман Samsung із дисплеєм Dynamic AMOLED 2X 120Гц, потужним процесором та системою камер з AI‑обробкою.\n\nЗахист IP68, швидка зарядка.",
            "category": "smartphones",
            "brand": "samsung",
        },
        {
            "name": "MacBook Air 13\" M2",
            "slug": "macbook-air-m2",
            "price": 1199.0,
            "discount_percent": 5,
            "image_url": "https://support.apple.com/library/APPLE/APPLECARE_ALLGEOS/SP858/mb-air-m2.png",
            "short_desc": "8‑ядерний CPU",
            "description": "MacBook Air на чипі M2 — легкий ноутбук із тривалим часом роботи, чудовою клавіатурою та Retina‑екраном. Ідеальний для навчання та роботи.",
            "category": "laptops",
            "brand": "apple",
        },
        {
            "name": "Google Pixel 8",
            "slug": "pixel-8",
            "price": 649.0,
            "discount_percent": 15,
            "image_url": "https://fdn2.gsmarena.com/vv/pics/google/google-pixel-8-1.jpg",
            "short_desc": "Tensor G3",
            "description": "Pixel 8 — чистий Android, камера з легендарною нічною зйомкою, процесор Tensor G3 з AI‑функціями та безпекою Google.",
            "category": "smartphones",
            "brand": "google",
        },
        {
            "name": "iPad Air 11\"",
            "slug": "ipad-air-11",
            "price": 599.0,
            "discount_percent": 5,
            "image_url": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/ipad-air-storage-select-202405-11in-starlight?wid=800&hei=800&fmt=jpeg&qlt=90&.v=1713977150625",
            "short_desc": "Liquid Retina, M2",
            "description": "iPad Air 11\" на чипі M2 — легкий та потужний планшет для навчання й творчості.",
            "category": "tablets",
            "brand": "apple",
        },
        {
            "name": "Apple Watch Series 9",
            "slug": "apple-watch-s9",
            "price": 399.0,
            "discount_percent": 0,
            "image_url": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/MP6V3ref_VW_34FR+watch-case-45-alum-starlight-nc-s9_VW_34FR+watch-face-45-starlight-s9_VW_34FR_GEO_EMEA?wid=800&hei=800&fmt=jpeg&qlt=90&.v=1693189671710",
            "short_desc": "Датчики здоров'я",
            "description": "Apple Watch S9 — відстеження активності, серця та сну, швидкий чип S9.",
            "category": "smartwatches",
            "brand": "apple",
        },
        {
            "name": "LG OLED C3 55\"",
            "slug": "lg-oled-c3-55",
            "price": 1299.0,
            "discount_percent": 12,
            "image_url": "https://www.lg.com/us/images/tvs/md07561822/gallery/medium01.jpg",
            "short_desc": "4K OLED, 120Гц",
            "description": "Справжній чорний колір і плавність 120Гц для кіно та ігор.",
            "category": "tvs",
            "brand": "samsung",  # бренд для прикладу; можна додати LG як бренд, але тримаємо коротко
        },
        {
            "name": "Навушники Bluetooth",
            "slug": "bt-headphones",
            "price": 79.0,
            "discount_percent": 20,
            "image_url": "https://resource.logitech.com/content/dam/logitech/en/products/headsets/h540/usb-headset-h540-gallery-1.png",
            "short_desc": "До 30 годин роботи",
            "description": "Легкі бездротові навушники з шумозаглушенням.",
            "category": "accessories",
            "brand": "logitech",
        },
    ]

    slug_to_cat = {c.slug: c.id for c in db.query(Category).all()}
    slug_to_brand = {b.slug: b.id for b in db.query(Brand).all()}

    for p in demo_products:
        existing = db.query(Product).filter_by(slug=p["slug"]).first()
        if not existing:
            db.add(
                Product(
                    name=p["name"],
                    slug=p["slug"],
                    price=p["price"],
                    discount_percent=p["discount_percent"],
                    image_url=p["image_url"],
                    short_desc=p["short_desc"],
                    description=p.get("description"),
                    category_id=slug_to_cat[p["category"]],
                    brand_id=slug_to_brand[p["brand"]],
                )
            )
        else:
            # форс-оновлення опису/зображення/короткого опису
            existing.description = p.get("description", existing.description)
            existing.image_url = p.get("image_url", existing.image_url)
            existing.short_desc = p.get("short_desc", existing.short_desc)
            db.add(existing)

    db.commit()
    db.close()


if __name__ == "__main__":
    run()




