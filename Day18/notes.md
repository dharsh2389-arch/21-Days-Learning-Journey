Modules and Packages in Python:

1. What is a Module?
A module is a Python file containing reusable code such as:
functions
variables
classes
Modules help break large programs into smaller manageable files.
Example module file:
calculator.py

2. Why Modules are Important
Advantages:
Code reuse
Better program organization
Easier debugging
Avoid writing duplicate code
Modules are used in real applications such as:
web development
automation scripts
machine learning programs
data analysis systems

3. Creating a Module
Create a Python file:
operations.py
Code:
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b
This file becomes a module.

4. Importing a Module
Create another file:


main.py
Code:
import operations

print(operations.add(10,5))
print(operations.multiply(3,4))
Output
15
12

5. Import Specific Functions
Instead of importing everything:
from operations import add, multiply

print(add(10,5))
print(multiply(4,2))

6. Import Using Alias

import operations as op

print(op.add(5,3))
Alias makes module names shorter.

7. Built-in Python Modules
Python includes many built-in modules.
Module     Purpose
math       mathematical operations
random     random numbers
datetime   date and time
os         operating system operations
sys        system functions
Example – math Module

import math

print(math.sqrt(36))
print(math.factorial(5))
Output
6.0
120
Example – random Module

import random

print(random.randint(1,10))
Output example
8

8. What is a Package?
A package is a folder that contains multiple modules.
It helps organize large projects.
Example structure:

project/
│
├── math_operations/
│     ├── add.py
│     ├── subtract.py
│
└── main.py
Here math_operations is a package.

9. Importing from a Package
Example:

project/
│
├── utilities/
│     ├── calculator.py
│
└── main.py
Code in main.py

from utilities.calculator import add

print(add(5,4))

10. The __name__ Variable
Every Python module has a built-in variable:

__name__
Example:
Python
Copy code
def greet():
    print("Hello Python")

if __name__ == "__main__":
    greet()
