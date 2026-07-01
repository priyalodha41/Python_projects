class Users:
    
    next_id=1;
    
    def __init__(self, name, email, phone,password,address):
        self.id = Users.next_id
        Users.next_id += 1
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.__password = password
        
    def display_profile(self):
        print(f"User ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
    
    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print("Old password is incorrect.")
            
    def update_address(self, new_address):
        self.address = new_address
        print("Address updated successfully.")
        
    def login(self, email, password):
        if self.email == email and self.__password == password:
            print("Login successful.")
        else:
            print("Invalid email or password.")
    def logout(self):
        print("Logout successful.")