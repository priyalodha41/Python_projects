class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @property
    def subtotal(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        for item in self.items:
            if item.product.name == product.name:
                if item.quantity + quantity > product.stock:
                    available = product.stock - item.quantity
                    print(f"Cannot add {quantity} more of '{product.name}'. Only {available} left in stock.")
                    return False
                item.quantity += quantity
                return True

        if quantity > product.stock:
            print(f"Only {product.stock} unit(s) of '{product.name}' are available.")
            return False

        self.items.append(CartItem(product, quantity))
        return True

    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name.strip().lower() == product_name.strip().lower():
                self.items.remove(item)
                return True
        return False

    def total(self):
        return sum(item.subtotal for item in self.items)

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.product.name} x {item.quantity} = \u20b9{item.subtotal:.2f}")
        print(f"Cart Total: \u20b9{self.total():.2f}")

    def clear(self):
        self.items = []

    def __len__(self):
        return len(self.items)