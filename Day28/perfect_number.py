num = int(input("Enter number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")

'''
Ouput
Enter number: 6
Perfect number
'''
