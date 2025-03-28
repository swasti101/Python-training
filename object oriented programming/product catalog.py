class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_details(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"

class Electronics(Product):
    def __init__(self, name, price, stock, brand, warranty):
        super().__init__(name, price, stock)
        self.brand = brand
        self.warranty = warranty

    def show_details(self):
        return f"{super().show_details()}, Brand: {self.brand}, Warranty: {self.warranty} years"

class Clothing(Product):
    def __init__(self, name, price, stock, material, size):
        super().__init__(name, price, stock)
        self.material = material
        self.size = size

    def show_details(self):
        return f"{super().show_details()}, Material: {self.material}, Size: {self.size}"

# Testing
laptop = Electronics("Laptop", 50000, 10, "Dell", 2)
shirt = Clothing("Shirt", 1500, 30, "Cotton", "L")

print(laptop.show_details())
print(shirt.show_details())
