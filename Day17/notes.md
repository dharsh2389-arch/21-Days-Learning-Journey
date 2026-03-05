List Comprehension, Lambda Functions & Built-in Functional Tools

1️. List Comprehension
List comprehension allows you to create lists in a single line instead of using loops.
Normal way (using loop)
numbers = [1,2,3,4,5]
squares = []
for n in numbers:
    squares.append(n*n)
print(squares)

Output
[1,4,9,16,25]
Using List Comprehension
numbers = [1,2,3,4,5]
squares = [n*n for n in numbers]
print(squares)
With Condition
Example: get even numbers
numbers = [1,2,3,4,5,6]
even = [n for n in numbers if n % 2 == 0]
print(even)

Output
[2,4,6]

2️. Dictionary Comprehension
Create dictionaries easily.
numbers = [1,2,3,4]
squares = {n: n*n for n in numbers}
print(squares)

Output
{1:1, 2:4, 3:9, 4:16}

3️. Lambda Functions
A lambda function is a small anonymous function.
Syntax
lambda arguments : expression

Example
add = lambda a,b: a+b
print(add(5,3))
Output
8

4️. map()
Used to apply a function to every element.

Example
numbers = [1,2,3,4]
result = list(map(lambda x: x*2, numbers))
print(result)

Output
[2,4,6,8]

5️. filter()
Used to filter elements.
Example
numbers = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0, numbers))
print(even)

Output
[2,4,6]

6️. zip()
Combine multiple lists.
names = ["Dharshini","Arun","Meena"]
marks = [90,85,88]
combined = list(zip(names,marks))
print(combined)

Output
[('Dharshini',90), ('Arun',85), ('Meena',88)]

7️. enumerate()
Adds index to loop.
students = ["A","B","C"]
for index, name in enumerate(students):
    print(index, name)

Output
0 A
1 B
2 C
