'''Electricity Bill Real-Time System
Question Statement:
Design an Electricity Billing System using Python operators:
=>Take customer name
=>Take number of units consumed
=>Charge ₹6 per unit
=>Add 5% electricity tax
=>Add fixed meter charge ₹150
=>Calculate total payable amount
=>Display complete bill'''

print("=== Electricity Billing System ===")

customername = input("Enter Customer Name: ")
noofunits = float(input("Enter Units Consumed: "))

# Cost per unit
costperunit = 6

unitamount = noofunits * costperunit

# Electricity tax 5%
tax = unitamount * (5 / 100)

# Fixed meter charge
metercharge = 150

# Total bill
totalbill = unitamount + tax + metercharge

print("\n--- Electricity Bill ---")
print("Customer Name:", customername)
print("Units Consumed:", noofunits)
print("Basic Amount:", unitamount)
print("Tax:", tax)
print("Meter Charge:", metercharge)
print("Total Bill:", totalbill)
