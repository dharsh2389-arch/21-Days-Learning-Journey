a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max = max(a, b)
while True:
    if max % a == 0 and max % b == 0:
        print("LCM:", max)
        break
    max+= 1

'''Output
Enter first number: 12
Enter second number: 9
LCM: 36
'''
