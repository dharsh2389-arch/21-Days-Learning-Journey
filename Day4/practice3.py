'''Shopping Mall Billing System
Question Statement:
Design a Shopping Mall Billing System using Python operators:
=>Take customer name
=>Take price and quantity of 3 items
=>Calculate subtotal
=>Apply:
  5% GST
  10% Service Tax
  2% City Tax
=>Add fixed packaging charge ₹100
=>Calculate total bill
=>Apply 5% membership discount
=>Display final payable amount'''

print("=== Shopping Mall Billing System ===")

customername = input("Enter Customer Name: ")

# Taking price and quantity
price1 = float(input("Enter Price of Item 1: "))
qty1 = int(input("Enter Quantity of Item 1: "))
price2 = float(input("Enter Price of Item 2: "))
qty2 = int(input("Enter Quantity of Item 2: "))
price3 = float(input("Enter Price of Item 3: "))
qty3 = int(input("Enter Quantity of Item 3: "))

total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3

subtotal = total1 + total2 + total3

# Taxes
gst = subtotal * (5 / 100)
servicetax = subtotal * (10 / 100)
citytax = subtotal * (2 / 100)


packagingcharge = 100

# Total before discount
beforediscount = subtotal + gst + servicetax + citytax + packagingcharge

# Membership discount 5%
discount = beforediscount * (5 / 100)

# Final amount
finalamount = beforediscount - discount


print("\n--- Billing Summary ---")
print("Customer Name:", customername)
print("Subtotal:", subtotal)

print("\nGST:", gst)
print("Service Tax:", servicetax)
print("City Tax:", citytax)
print("Packaging Charge:", packagingcharge)

print("\nTotal Before Discount:", beforediscount)
print("Discount:", discount)
print("Final Amount Payable:", finalamount)
