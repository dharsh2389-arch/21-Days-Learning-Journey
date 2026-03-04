print("Division Calculator")
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
except ValueError:
    print("Invalid number entered")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Calculation complete")

'''
Output 1:
Division Calculator
Enter first number: ds
Invalid number entered
Calculation complete

Output 2:
Division Calculator
Enter first number: 346
Enter second number: 0
Cannot divide by zero
Calculation complete

Output 3:
Division Calculator
Enter first number: 15
Enter second number: 5
Result: 3.0
Calculation complete
'''
