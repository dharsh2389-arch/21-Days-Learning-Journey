a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
c=int(input("Enter side c: "))
if (a + b > c)and(a + c > b)and(b + c > a):
    print("Valid Triangle")
else:
    print("Not Valid Triangle")

'''
Output
Enter side a: 6
Enter side b: 3
Enter side c: 4
Valid Triangle
'''
