'''Create a product system:
Base Class → Product
name
private price
get_price()
set_price() (only allow price > 0)
Child Class → Electronics
warranty_years
Override get_price() to add 18% GST
Child Class → Clothing
size
Override get_price() to add 5% GST'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")
class Electronics(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years
    def get_price(self):
        base_price = super().get_price()
        gst_price = base_price + (base_price * 0.18)
        return gst_price
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    def get_price(self):
        base_price = super().get_price()
        gst_price = base_price + (base_price * 0.05)
        return gst_price
e1 = Electronics("Laptop", 50000, 2)
c1 = Clothing("Shirt", 1000, "M")
print("Electronics Final Price:", e1.get_price())
print("Clothing Final Price:", c1.get_price())

'''Output:
Electronics Final Price: 59000.0
Clothing Final Price: 1050.0'''
