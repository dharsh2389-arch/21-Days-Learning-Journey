'''Question
Create a shopping cart system where user enters 4 product prices and program calculates:
Total bill
Highest priced item
Lowest priced item'''

print("Shopping Cart System\n")
cart=[]
for i in range(1,6):
    items=float(input("Enter the price of the item " + str(i) + ": "))
    cart.append(items)
print("Total Price: ",sum(cart))
print("Highest Price: ",max(cart))
print("Lowest Price: ",min(cart))
