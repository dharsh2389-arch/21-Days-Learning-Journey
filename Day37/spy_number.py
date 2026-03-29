'''
Spy Number:
A number is called a Spy Number if: Sum of digits = Product of digits
'''

num = input("Enter a number: ")
sum = 0
product = 1
for digit in num:
    d = int(digit)
    sum += d
    product *= d
if sum == product:
    print("Spy Number")
else:
    print("Not a Spy Number")

'''
Output
Enter a number: 123
Spy Number
'''
