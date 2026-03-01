'''Create a class Rectangle with:

length

width

Add method:

area() → returns area

display() → prints length, width, area'''

class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
   
  def area(self):
    area=self.length * self.width
    return area
  def display(self):
    print("Length: ",self.length)
    print("Width: ",self.width)
    print("Area: ",self.area())
r1=Rectangle(10,5)
r1.display()

'''Output
Length:  10
Width:  5
Area:  50'''
