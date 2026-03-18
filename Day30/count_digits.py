num = int(input("Enter number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)

'''Output
Enter number: 7394949
Number of digits: 7
'''
