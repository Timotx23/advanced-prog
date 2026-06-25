# Consider the following dataset with products and their prices, similar to the one from the first lecture (but larger):
products = [
    ("Laptop", "electronics", 899),
    ("Smartphone", "electronics", 699),
    ("Tablet", "electronics", 449),
    ("Headphones", "electronics", 149),
    ("Smart TV", "electronics", 599),
    ("Gaming Console", "electronics", 499),
    ("Winter Jacket", "clothing", 120),
    ("Jeans", "clothing", 65),
    ("Sneakers", "clothing", 85),
    ("T-Shirt", "clothing", 25),
    ("Dress", "clothing", 95),
    ("Sweater", "clothing", 55),
    ("Sofa", "furniture", 1200),
    ("Dining Table", "furniture", 450),
    ("Office Chair", "furniture", 280),
    ("Bed Frame", "furniture", 350),
    ("Bookshelf", "furniture", 180),
    ("Washing Machine", "appliances", 550),
    ("Refrigerator", "appliances", 850),
    ("Microwave", "appliances", 120),
    ("Vacuum Cleaner", "appliances", 180),
    ("Coffee Maker", "appliances", 95),
    ("Tent", "outdoor equipment", 220),
    ("Sleeping Bag", "outdoor equipment", 75),
    ("Camping Stove", "outdoor equipment", 60),
    ("Bicycle", "outdoor equipment", 450),
    ("Grill", "outdoor equipment", 320),
    ("Backpack", "backpacks", 45),
    ("Laptop Bag", "backpacks", 55),
    ("Travel Backpack", "backpacks", 85),
    ("Chocolate Box", "chocolates", 15),
    ("Jewelry Set", "jewelry", 250),
    ("Watch", "jewelry", 180),
    ("School Supplies Set", "school supplies", 35),
    ("Toy Car", "toys", 25),
    ("Board Game", "toys", 40),
    ("Action Figure", "toys", 20),
    ("Garden Tools Set", "gardening supplies", 75),
    ("Patio Chair", "outdoor furniture", 120),
    ("Mattress", "mattresses", 650),
    ("Fresh Vegetables", "food", 4.00),
    ("Fresh Fruit", "food", 5.50),
    ("Pasta", "food", 1.80),
    ("Mozzarella", "food", 6.50),
    ("Novel", "books", 15.00),
    ("Textbook", "books", 45.00),
    ("Children's Book", "books", 12.00),
    ("Cough Syrup", "medicine", 12.00),
    ("First Aid Kit", "medicine", 20.00),
    ("Diapers", "baby products", 25.00),
    ("Children's Car Seat", "baby products", 120.00),
    ("Bus Ticket", "transport", 3.00),
    ("Museum Ticket", "culture", 12.00),
    ("Bicycle Helmet", "safety equipment", 40.00),
    ("Children's Shoes", "children's clothing", 35.00),
    ("Children's Jacket", "children's clothing", 45.00)
]

# Below are the standard and reduced VATs for 21 countries in Europe.
standard_vat = {
    "Germany": 19,
    "France": 20,
    "Italy": 22,
    "Spain": 21,
    "Netherlands": 21,
    "Belgium": 21,
    "Austria": 20,
    "Sweden": 25,
    "Poland": 23,
    "Portugal": 23,
    "Greece": 24,
    "Czech Republic": 21,
    "Hungary": 27,
    "Denmark": 25,
    "Finland": 25.5,
    "Norway": 25,
    "Ireland": 23,
    "Croatia": 25,
    "Switzerland": 8.1,
    "United Kingdom": 20,
    "Bulgaria": 20
}

reduced_vat = {
    "France": 5.5,
    "Italy": 4, 
    "Spain": 4, 
    "Netherlands": 9,
    "Belgium": 6,
    "Austria": 10,
    "Sweden": 6, 
    "Poland": 5, 
    "Portugal": 6,
    "Greece": 6, 
    "Czech Republic": 10,
    "Hungary": 5,
    "Finland": 10,
    "Norway": 12, 
    "Ireland": 9, 
    "Croatia": 5, 
    "Switzerland": 2.6,
    "United Kingdom": 5,
    "Bulgaria": 9
}

reduced_vat_categories = [
    "chocolates", 
    "school supplies",
    "food",
    "books",
    "medicine",
    "baby products",
    "transport",
    "culture",
    "children's clothing"

]

seasonal_discounts = {
    "January": {
        "name": "New Year Sales / Winter Clearance",
        "discount": 30,
        "categories": ["clothing", "electronics", "fitness equipment"]
    },
    "February": {
        "name": "Valentine's Day / Presidents' Day Sales",
        "discount": 20,
        "categories": ["jewelry", "flowers", "chocolates", "furniture", "appliances"]
    },
    "March": {
        "name": "Spring Sales / End of Winter",
        "discount": 25,
        "categories": ["winter clothing", "home goods", "gardening supplies"]
    },
    "April": {
        "name": "Easter / Spring Fashion",
        "discount": 15,
        "categories": ["clothing", "candy", "toys", "outdoor furniture"]
    },
    "May": {
        "name": "Memorial Day Sales",
        "discount": 25,
        "categories": ["mattresses", "appliances", "outdoor equipment", "grills"]
    },
    "June": {
        "name": "Summer Sales / Mid-Year Clearance",
        "discount": 20,
        "categories": ["summer clothing", "camping gear", "electronics"]
    },
    "July": {
        "name": "Independence Day / Summer Clearance",
        "discount": 30,
        "categories": ["outdoor furniture", "grills", "electronics", "clothing"]
    },
    "August": {
        "name": "Back to School",
        "discount": 20,
        "categories": ["school supplies", "clothing", "electronics", "backpacks"]
    },
    "September": {
        "name": "Labor Day / Fall Preview",
        "discount": 25,
        "categories": ["appliances", "furniture", "summer clearance"]
    },
    "October": {
        "name": "Halloween / Fall Sales",
        "discount": 15,
        "categories": ["costumes", "candy", "decorations", "fall clothing"]
    },
    "November": {
        "name": "Black Friday / Cyber Monday",
        "discount": 50,
        "categories": ["electronics", "toys", "clothing", "appliances", "almost everything"]
    },
    "December": {
        "name": "Christmas / Holiday Sales / End of Year Clearance",
        "discount": 40,
        "categories": ["toys", "electronics", "clothing", "decorations", "gift items"]
    }
}

members = { # Discount in %.
    "golden": 20,
    "silver": 10,
    "bronze": 5
}