def greet():
    print("Welcome to Python Learning")

greet()

def add(a, b):
    print("Addition:", a + b)

add(10, 20)

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)

def power(base, exponent=2):
    return base ** exponent

print("Square:", power(6))
print("Cube:", power(6, 3))
