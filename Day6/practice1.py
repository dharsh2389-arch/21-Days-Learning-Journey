'''Question
Design a Mini Banking Transaction System.
Take initial account balance.
Allow exactly 5 transactions.
In each transaction:
Take deposit amount.
Take withdrawal amount.
Update the balance after each transaction.
Display final balance.
If final balance is less than ₹1000, display "Low Balance Alert", otherwise display "Account Safe".'''

print("Mini Banking Transaction System\n")
name = input("Enter your name: ")
acno=int(input("Enter your Account Number: "))
balance = float(input("Enter Initial Balance: "))

for transaction in range(1, 6):
    print("\nTransaction",transaction)
    deposit = float(input("Enter Deposit Amount: "))
    withdrawal = float(input("Enter Withdrawal Amount: "))
    balance = balance + deposit
    balance = balance - withdrawal
    print("Current Balance:", balance)
print("\nName: ",name)
print("Account Number: ",acno)
print("Final Balance:", balance)

if balance < 1000:
    print("Status: Low Balance Alert")
else:
    print("Status: Account Safe")
