'''
A number is called a Strong Number if the sum of the factorial of its digits equals the number.
Example
Input: 145
Output: Strong Number
Explanation
1! + 4! + 5! = 1 + 24 + 120 = 145
'''

num = int(input("Enter number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    temp //= 10
if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")

'''Output
Enter number: 40585
Strong Number
'''
