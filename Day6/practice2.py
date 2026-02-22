'''Question
Design an Inventory Stock Monitoring System for a store.
Take initial stock quantity.
Track sales for 7 days.
For each day:
Take number of items sold.
Subtract sold items from stock.
Display remaining stock after each day.
At the end:
If stock is less than or equal to 10, display "Low Stock Warning".
Otherwise display "Stock Level Sufficient".'''

print("Inventory Stock Monitoring System\n")

stock = int(input("Enter Initial Stock: "))

for day in range(1, 8):
    sold = int(input("Enter Items Sold on Day " + str(day) + ": "))
    stock = stock - sold
    print("Remaining Stock after Day", day, ":", stock)

print("\nFinal Stock:", stock)

if stock <= 10:
    print("Low Stock Warning")
else:
    print("Stock Level Sufficient")
