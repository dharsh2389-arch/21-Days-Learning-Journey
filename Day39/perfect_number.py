'''
A number is Perfect if: Sum of its proper divisors = number
'''

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect")

'''
Enter a number: 6
Perfect Number
'''
