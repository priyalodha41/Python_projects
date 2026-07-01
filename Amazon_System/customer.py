from cart import Cart


class Customer:
    def __init__(self, name, email, phone, password, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
        self.cart = Cart()
        self.orders = []

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"