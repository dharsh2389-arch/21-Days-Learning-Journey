'''Create a class BankAccount.
Add:
deposit()
withdraw()
check_balance()
Try to prevent withdrawal if balance is low.'''

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

acc = BankAccount("Dharshini", 10000)

acc.deposit(2000)
acc.withdraw(1500)
acc.check_balance()

'''Output
Account Holder: Dharshini
Balance: 10500'''
