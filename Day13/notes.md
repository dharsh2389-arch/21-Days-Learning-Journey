OOP in Python

What is OOP?
OOP is a way of writing programs by modeling real-world things.

Instead of writing only functions, we create:
-> Class: Blueprint
-> Object: Real instance created from blueprint

Example: Blueprint of house - Class
         Actual house       - Object

Class:
class Student:
  pass
#This creates a class but it does nothing.

Object:
s1=Student()
#Now s1 is an object of Student.

Constructor:
Constructor runs automatically when object is creaated. 
Used to initialize values.

class Student: 
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
s1=Student("Dharshini",95)
print(s1.name)
print(s1.marks)

What is self?
self refers to the current object.
Each object stores its own data.

Example:
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Dharshini")
s2 = Student("Reena")
print(s1.name)
print(s2.name)

Methods:
Functions inside class.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1 = Student("Dharshini", 90)
s1.display()
