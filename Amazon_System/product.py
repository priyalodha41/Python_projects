class Product:
    def __init__(self, name, price, description, brand, rating, category):
        self.name = name
        self.price = price
        self.description = description
        self.brand = brand
        self.rating = rating
        self.category = category
        self.stock = 0

    def increase_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity to add cannot be negative.")
        self.stock += quantity

    def decrease_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError(f"Insufficient stock for '{self.name}'. Available: {self.stock}")
        self.stock -= quantity

    def __str__(self):
        return (f"{self.name} | Brand: {self.brand} | Price: \u20b9{self.price:.2f} | "
                f"Rating: {self.rating}/5 | Stock: {self.stock} | Category: {self.category.category_name}")