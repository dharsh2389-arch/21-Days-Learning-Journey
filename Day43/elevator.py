c = int(input("Enter current floor: "))
r = int(input("Enter requested floor: "))
if r > c:
    print("Go Up")
elif r < c:
    print("Go Down")
else:
    print("Stay on the same floor")

'''
Output
Enter current floor: 5
Enter requested floor: 8
Go Up
'''
