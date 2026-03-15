num = int(input("Enter number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

'''
Output
Enter number: 100
Reversed number: 1
'''
