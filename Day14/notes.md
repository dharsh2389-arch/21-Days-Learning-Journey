OOPS
1. Ecapsulation:
     Hiding internal data and access.
   We access private variables using __
   Example:
   class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   #private variable
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
  acc = BankAccount("Dharshini", 10000)
  acc.deposit(2000)
  print("Balance:", acc.get_balance())
  
  ( If we try to print private varible like print(self.__balance) -> It shows error ) -> This may protect datas.
  
2. Inheritance:
     Inheritance allows one class to reuse properties and methods another class.
     Parent class - Base class
     Child class - Derived class
   Why use inheritance?
     -> Code reuse
     -> Reduce duplication
     -> Maintain hierarchy
     -> Real-world modeling
   Example:
   class Person:
     def __init__(self, name):
       self.name=name
     def greet(self):
       print("Hello", self.name)
   class Student(Person):
     pass
   s1 = Student("Dharshini")
   s1.greet()

Student inherits greet() from Person.

Types of Inheritance in Python:
1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance

i. Single Inheritance:
  One parent -> One child
  Example:
  class Parent:
    pass
  class Child(Parent):
    pass

ii. Multilevel Inheritance:
  A -> B -> C
  Example:
  class Grandparent:
    pass
  class Parent(Grandparent):
    pass
  class Child(Parent):
    pass

iii. Hierarchical Inheritance:
  One parent -> Multiple Children
  Example: 
  class Person:
    pass
  class Child1(Person):
    pass
  class Child2(Person):
    pass

iv. Multiple Inheritance:
  One child -> Multiple Parents
  Example:
  class Father:
    def skills(self):
      print("Gardeninng")
  class Mother:
    def skills(self):
      print("Cooking")
  class Child(Father, Mother):
    pass

v. Hybrid Inheritance:
  Combination of two or more types of inheritance.
  Example: Hierarchical + Multiple
  class A:
    def show(self):
      print("Class A")
  class B(A):
    pass
  class C(A):
    pass
  class D(B,C):
    pass

3. Method Overriding:
   When child class defines a method with same name as parent class.
   The child version replaces theparent version.
   Example:
   class Person:
     def role(self):
       print("I am a Person")
  class Student(Person):
    def role(self):
      print("I am a Student")
  p=Person()
  s=Student()
  p.role()
  s.role()

4. Polymorphism:
   One interface, multiple implementations. [Same method name, different behaviour]
   Example:
   class Dog:
     def sound(self):
       print("Bark")
   class Cat:
     def sound(self):
       print("Meow")
   animals=[Dog(), Cat()]
   for animal in animals:
     animal.sound()

Types of Polymorphism:
1. Method Overriding
2. Duck Typing
3. Operator Overloading

i. Method Overriding
Example:
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()

ii. Duck Typing:
    Example:
    class Bird:
    def fly(self):
        print("Bird flies")
class Airplane:
    def fly(self):
        print("Airplane flies")
def start_flying(obj):
    obj.fly()
start_flying(Bird())
start_flying(Airplane())

iii. Operator Overloading
    Example:
    print(5 + 3)  
    print("Hi " + "All")  
    print([1,2] + [3,4]) 

    Here, + operator is used to add all integers, strings, lists.


5. super() Keyword:
   Used to call parent class Constructors and methods inside child class.
   Example:
   class Person:
    def __init__(self, name):
        self.name = name
  class Student(Person):
      def __init__(self, name, marks):
          super().__init__(name)
          self.marks = marks
      def display(self):
          print(self.name, self.marks)
  s = Student("Dharshini", 95)
  s.display()
