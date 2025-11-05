from app import db, Fragrance, app

with app.app_context():
    db.drop_all()      # optional: clears existing data
    db.create_all()    # creates tables if they don't exist

    # Sample fragrances in your display order
    fragrances = [
        Fragrance(name="Gucci Guilty Pour Homme", notes="Citrus, Lavender, Lemon", price="$100", bottle_size="100ml"),
        Fragrance(name="Dior Homme 2020", notes="Iris, Vetiver, Amber", price="$125", bottle_size="100ml"),
        Fragrance(name="Coach for Men", notes="Bergamot, Green Apple, Cedar", price="$85", bottle_size="100ml"),
        Fragrance(name="Valentino Born in Roma Intense", notes="Vanilla, Woody, Amber", price="$140", bottle_size="100ml"),
        Fragrance(name="Valentino Yellow Dream", notes="Citrus, Musk, Jasmine", price="$140", bottle_size="100ml"),
        Fragrance(name="Valentino Coral Fantasy", notes="Fruity, Sweet, Floral", price="$140", bottle_size="100ml"),
        Fragrance(name="Valentino Uomo Intense", notes="Iris, Leather, Vanilla", price="$140", bottle_size="100ml"),
        Fragrance(name="Azzaro The Most Wanted Intense", notes="Rum, Amber, Tonka Bean", price="$110", bottle_size="100ml"),
        Fragrance(name="Kilian Black Phantom", notes="Rum, Coffee, Dark Chocolate", price="$350", bottle_size="50ml"),
        Fragrance(name="Chanel Allure Homme Edition Blanche", notes="Citrus, Musk, Vetiver", price="$150", bottle_size="100ml"),
        Fragrance(name="Parfums de Marly Greenley", notes="Fruity, Floral, Musk", price="$250", bottle_size="100ml"),
        Fragrance(name="Jean Paul Gaultier Le Beau Le Parfum", notes="Coconut, Tonka Bean, Amber", price="$130", bottle_size="125ml")
    ]

    db.session.add_all(fragrances)
    db.session.commit()
    print("Sample fragrances added!")
