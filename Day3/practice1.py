#Temperature converter

print("*** Temperature Converter ***")
celsius = float(input("Enter temperature in Celsius: "))
#Formula for fahrenheit = (celsius*9/5)+32
fahrenheit = (celsius * 9/5) + 32
#converting fahrenheit to a string for display
fahrenheit_str = str(round(fahrenheit, 2))
print("Temperature in Fahrenheit:", fahrenheit_str)
is_hot = bool(celsius > 30)
print("Is it a hot day?", is_hot)

'''Conversion types used here is: 
1. string - input() to return a string
2. float - to return a decimal valueas as temperature can be in decimal
3. bool - To return true or false to check whether temperature is high or low'''
