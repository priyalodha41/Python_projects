from users import Users

class Admin(Users):
    
    def __init__(self, name, email, phone, password, address,role,permissions):
        super().__init__(name, email, phone, password, address)
        self.role = role
        self.permissions = permissions

    def add_product(self):
        # Logic to add a new product
        pass
    
    def remove_product(self, product_id):
        # Logic to remove a product by ID
        pass
    
    def update_product_info(self, product_id, new_info):
        # Logic to update product information
        pass
    
    def view_all_products(self):
        # Logic to view all products
        pass