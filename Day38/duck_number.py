'''
A number is called a Duck Number if: It contains at least one ‘0’
But should not start with 0
'''

num = input("Enter a number: ")
if num[0] == '0':
    print("Invalid number")
elif '0' in num:
    print("Duck Number")
else:
    print("Not a Duck Number")

'''
Output
Enter a number: 2026
Duck Number
'''
