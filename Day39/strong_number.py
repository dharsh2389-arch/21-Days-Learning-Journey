'''
A number is Strong if: Sum of factorial of digits = number
'''

num = input("Enter a number: ")
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
sum = 0
for digit in num:
    sum += factorial(int(digit))
if sum == int(num):
    print("Strong Number")
else:
    print("Not Strong")

'''
Enter a number: 145
Strong Number
'''
