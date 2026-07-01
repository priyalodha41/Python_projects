class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def search_product(self, name):
        name = name.strip().lower()
        for product in self.products:
            if product.name.strip().lower() == name:
                return product
        return None

    def display_products(self):
        if not self.products:
            print("No products available.")
            return
        for index, product in enumerate(self.products, start=1):
            print(f"{index}. {product}")

    def __len__(self):
        return len(self.products)