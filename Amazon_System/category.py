class Category:
    def __init__(self, category_name, description):
        self.category_name = category_name
        self.description = description

    def __str__(self):
        return f"{self.category_name} - {self.description}"