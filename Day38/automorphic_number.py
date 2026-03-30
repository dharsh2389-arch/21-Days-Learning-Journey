'''
A number is Automorphic if its square ends with the same number.
'''

square = str(int(num) ** 2)
if square.endswith(num):
    print("Automorphic Number")
else:
    print("Not Automorphic")

'''
Output
Enter a number: 25
Automorphic Number
'''
