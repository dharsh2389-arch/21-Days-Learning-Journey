'''Question: Geometry Package
Create a package called geometry that contains modules to calculate areas of shapes.
Modules required:
circle.py
rectangle.py
triangle.py
Each module must contain a function to calculate area.
Then import them in a main program.'''

'''geometry'''
#circle.py
def area_circle(r):
    return 3.14 * r * r
  
#rectangle.py
def area_rectangle(l, w):
    return l * w
  
#triangle.py
def area_triangle(b, h):
    return 0.5 * b * h
  
'''geometry'''
#main.py
from circle import area_circle
from rectangle import area_rectangle
from triangle import area_triangle

r = float(input("Enter radius: "))
l = float(input("Enter length: "))
w = float(input("Enter width: "))
b = float(input("Enter base: "))
h = float(input("Enter height: "))

print("Area of Circle:", area_circle(r))
print("Area of Rectangle:", area_rectangle(l, w))
print("Area of Triangle:", area_triangle(b, h))

'''Output
Enter radius: 5
Enter length: 7
Enter width: 3
Enter base: 6
Enter height: 4
Area of Circle: 78.5
Area of Rectangle: 21.0
Area of Triangle: 12.0'''
