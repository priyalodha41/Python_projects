from customer import Customer
from category import Category
from product import Product
from inventory import Inventory
from order import Order
from payment import UPI, Card, CashOnDelivery


# ---------- Safe input helpers ----------
# These stop the program from crashing whenever someone types
# something that isn't a valid number.

def get_int(prompt, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Please enter a number less than or equal to {max_value}.")
            continue
        return value


def get_float(prompt, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Please enter a number less than or equal to {max_value}.")
            continue
        return value


def get_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


# ---------- Application state ----------
inventory = Inventory()
customers = []
categories = []
current_customer = None
current_order = None

MENU = """
        ============= AMAZON =============

        1  Register Customer
        2  Login
        3  Add Category
        4  Add Product
        5  View Categories
        6  View Products
        7  Search Product
        8  Add Product to Cart
        9  View Cart
        10 Checkout
        11 Payment
        12 View Orders
        13 Logout
        14 Exit

        ===================================
        """

while True:
    print(MENU)
    choice = get_int("Enter your choice : ")

    # ---------------- Register ----------------
    if choice == 1:
        name = get_nonempty("Enter Name : ")
        email = get_nonempty("Enter Email : ").lower()

        if any(c.email == email for c in customers):
            print("An account with this email already exists.")
            continue

        phone = get_nonempty("Enter Phone : ")
        password = get_nonempty("Enter Password : ")
        address = get_nonempty("Enter Address : ")

        customer = Customer(name, email, phone, password, address)
        customers.append(customer)
        print("Customer Registered Successfully.")

    # ---------------- Login ----------------
    elif choice == 2:
        email = input("Enter Email : ").strip().lower()
        password = input("Enter Password : ").strip()

        matched = next((c for c in customers if c.email == email), None)

        if matched and matched.password == password:
            current_customer = matched
            print(f"Welcome {matched.name}")
        else:
            print("Invalid Email or Password.")

    # ---------------- Add Category ----------------
    elif choice == 3:
        category_name = get_nonempty("Enter Category Name : ")
        description = get_nonempty("Enter Description : ")

        category = Category(category_name, description)
        categories.append(category)
        print("Category Added Successfully.")

    # ---------------- Add Product ----------------
    elif choice == 4:
        if not categories:
            print("No categories available. Please add a category first.")
            continue

        print("Available Categories:")
        for index, category in enumerate(categories, start=1):
            print(index, category.category_name)

        category_choice = get_int("Choose Category : ", min_value=1, max_value=len(categories))
        selected_category = categories[category_choice - 1]

        product_name = get_nonempty("Enter Product Name : ")
        price = get_float("Enter Price : ", min_value=0)
        description = get_nonempty("Enter Description : ")
        brand = get_nonempty("Enter Brand : ")
        rating = get_float("Enter Rating (0-5) : ", min_value=0, max_value=5)
        stock = get_int("Enter Stock Quantity : ", min_value=0)

        product = Product(product_name, price, description, brand, rating, selected_category)
        product.increase_stock(stock)
        inventory.add_product(product)
        print("Product Added Successfully.")

    # ---------------- View Categories ----------------
    elif choice == 5:
        if not categories:
            print("No categories available.")
        else:
            for category in categories:
                print(category)

    # ---------------- View Products ----------------
    elif choice == 6:
        print("Products in Inventory:")
        inventory.display_products()

    # ---------------- Search Product ----------------
    elif choice == 7:
        product_name = get_nonempty("Enter Product Name to Search : ")
        product = inventory.search_product(product_name)
        if product:
            print("Product Found:")
            print(product)
        else:
            print("Product Not Found.")

    # ---------------- Add Product to Cart ----------------
    elif choice == 8:
        if not current_customer:
            print("Please login first.")
            continue

        if len(inventory) == 0:
            print("No products available.")
            continue

        inventory.display_products()
        product_name = get_nonempty("Enter Product Name to Add to Cart : ")
        product = inventory.search_product(product_name)

        if not product:
            print("Product Not Found.")
            continue

        if product.stock == 0:
            print("This product is currently out of stock.")
            continue

        quantity = get_int("Enter Quantity : ", min_value=1)
        if current_customer.cart.add_item(product, quantity):
            print("Product Added To Cart Successfully.")

    # ---------------- View Cart ----------------
    elif choice == 9:
        if current_customer:
            current_customer.cart.display_cart()
        else:
            print("Please login first.")

    # ---------------- Checkout ----------------
    elif choice == 10:
        if not current_customer:
            print("Please login first.")
            continue

        if len(current_customer.cart) == 0:
            print("Cart is empty. Please add products to cart before checkout.")
            continue

        current_order = Order(current_customer, current_customer.cart)
        print("Order Created Successfully.")
        print(current_order)

    # ---------------- Payment ----------------
    elif choice == 11:
        if not current_customer:
            print("Please login first.")
            continue

        if not current_order:
            print("No order found. Please checkout first.")
            continue

        print("Choose Payment Method:")
        print("1. UPI")
        print("2. Card")
        print("3. Cash on Delivery")
        payment_choice = get_int("Enter your choice : ", min_value=1, max_value=3)

        if payment_choice == 1:
            upi_id = get_nonempty("Enter UPI ID : ")
            payment_method = UPI(current_order.total_amount, upi_id)
        elif payment_choice == 2:
            card_holder = get_nonempty("Enter Card Holder Name : ")
            card_number = get_nonempty("Enter Card Number : ")
            expiry_date = get_nonempty("Enter Expiry Date (MM/YY) : ")
            payment_method = Card(current_order.total_amount, card_number, card_holder, expiry_date)
        else:
            payment_method = CashOnDelivery(current_order.total_amount)

        payment_method.pay()
        payment_method.display_payment()

        current_order.update_status("Delivered" if payment_choice != 3 else "Confirmed (COD)")
        print("Payment Successful.")
        current_order = None

    # ---------------- View Orders ----------------
    elif choice == 12:
        if current_customer is None:
            print("Please login first.")
        elif not current_customer.orders:
            print("No Orders Found.")
        else:
            for order in current_customer.orders:
                print(order)

    # ---------------- Logout ----------------
    elif choice == 13:
        if current_customer:
            current_customer = None
            current_order = None
            print("Logout Successful.")
        else:
            print("No customer is currently logged in.")

    # ---------------- Exit ----------------
    elif choice == 14:
        print("Thank You For Using Amazon!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 14.")