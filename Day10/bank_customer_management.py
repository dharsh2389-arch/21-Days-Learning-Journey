'''Question Statement
Design a Bank Customer Management System using Dictionary.
The system should:
Create an empty customer record.
Add customer details (account number, name, balance, branch).
Update balance after deposit.
Use:
keys()
values()
items()
get()
update()
pop()
clear()
Display customer summary.
Remove a field.
Clear complete record at the end.'''

print("Bank Customer Management System\n")
customer={}
customer["account_number"] = 1234567890
customer["name"] = "Dharshini"
customer["balance"] = 15000
customer["branch"] = "Nagercoil"

print("Customer Record:", customer)
deposit = 5000
customer["balance"] += deposit

print("\nAfter Deposit:", customer)

print("\nCustomer Name:", customer.get("name"))

print("\nKeys:", customer.keys())
print("\nValues:", customer.values())
print("\nItems:", customer.items())

customer.update({"account_type": "Savings"})
print("\nAfter Update:", customer)

customer.pop("branch")
print("\nAfter Removing Branch:", customer)

print("\nTotal Fields:", len(customer))

customer.clear()
print("\nAfter Clearing Record:", customer)
