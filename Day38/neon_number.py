'''
A number is Neon if: Sum of digits of its square = the number
'''

num = int(input("Enter a number: "))
square = num * num
sum = 0
for digit in str(square):
    sum += int(digit)
if sum == num:
    print("Neon Number")
else:
    print("Not Neon")

'''
Output
Enter a number: 9
Neon Number

Explanation
9² = 81
where 8 + 1 = 9
'''
