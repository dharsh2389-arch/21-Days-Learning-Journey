num = int(input("Enter number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("Sum of digits:", sum)

'''
Ouput
Enter number: 123
Sum of digits: 6
'''
