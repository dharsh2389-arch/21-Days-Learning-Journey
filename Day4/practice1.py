'''Hospital Billing System
Question Statement:
Design a Hospital Billing System using Python operators:
=>Take doctor consultation fee
=>Take room charge per day
=>Take number of days stayed
=>Take lab test charges
=>Take medicine charges
=>Calculate subtotal
=>Add 12% GST
=>Add 20% insurance coverage
=>Calculate final payable amount
=>Display billing summary'''

# Hospital Billing System

print("=== Hospital Billing System ===")
consultationfee = float(input("Enter Doctor Consultation Fee: "))
roomchargeperday = float(input("Enter Room Charge Per Day: "))
noofdays = int(input("Enter Number of Days Stayed: "))
labtest = float(input("Enter Lab Test Charges: "))
medicinecharge = float(input("Enter Medicine Charges: "))

# Room total
roomtotal = roomchargeperday * noofdays

# Subtotal
subtotal = consultationfee + roomtotal + labtest + medicinecharge

# GST 12%
gst = subtotal * (12 / 100)

# Total before insurance
totalbill = subtotal + gst

# Insurance 20%
insurance = totalbill * (20 / 100)

# Final payable
finalamount = totalbill - insurance

print("\n--- Billing Summary ---")
print("Subtotal:", subtotal)
print("GST:", gst)
print("Total Bill:", totalbill)
print("Insurance Cover:", insurance)
print("Final Amount Payable:", finalamount)
