'''Question: Temperature Conversion Module
Create a module called temperature.py that contains two functions:
Convert Celsius to Fahrenheit
Convert Fahrenheit to Celsius
Then create another program that imports the module and performs the conversions.
Formula:
F = (C × 9/5) + 32
C = (F − 32) × 5/9'''

#temperature.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

#main.py
import temperature

c = float(input("Enter temperature in Celsius: "))
f = float(input("Enter temperature in Fahrenheit: "))

print("Celsius to Fahrenheit:", temperature.celsius_to_fahrenheit(c))
print("Fahrenheit to Celsius:", temperature.fahrenheit_to_celsius(f))

'''
Output
Enter temperature in Celsius: 30
Enter temperature in Fahrenheit: 86
Celsius to Fahrenheit: 86.0
Fahrenheit to Celsius: 30.0
'''
