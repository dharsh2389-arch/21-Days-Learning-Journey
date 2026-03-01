'''Create a class Car with:

brand

price

Create 3 car objects.

Increase price of only one car manually and print all cars to confirm others are unchanged.'''

class Car:
  def __init__(self,brand,price):
    self.brand=brand
    self.price=price
  def display(self):
    print(self.brand,self.price)
c1=Car("BMW",500000000)
c2=Car("Mercedes",700000000)
c3=Car("Rolls Royce",10000000000)

c1.price+=5000000

c1.display()
c2.display()
c3.display()

'''Output
BMW 505000000
Mercedes 700000000
Rolls Royce 10000000000'''
