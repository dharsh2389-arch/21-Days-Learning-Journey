print("Calculator\n")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        raise ValueError("Invalid operator")
except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Calculation finished")

'''
Output:
Calculator

Enter first number: 50
Enter second number: 10
Enter operation (+, -, *, /): *
Result: 500.0
Calculation finished
'''
