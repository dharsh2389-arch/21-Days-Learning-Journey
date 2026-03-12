'''Create a class Book with:

title

price

When object is created, values should be initialized automatically.

Create 2 book objects and print their values'''

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
b1 = Book("Literature",500)
b2 = Book("Science",300)
print(b1.title,b1.price)
print(b2.title,b2.price)

'''Output
Literature 500
Science 300'''
