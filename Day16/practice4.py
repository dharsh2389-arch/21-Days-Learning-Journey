'''Question
Create a simple ATM system that:
Asks the user for:
name
amount to withdraw
Checks if withdrawal is valid.
Saves every transaction to a file called transactions.txt.
Uses exception handling to manage errors such as:
invalid amount
file errors
unexpected input
Each transaction should be appended to the file.
Example file content:
Copy code
Dharshini withdrew 500
Arun withdrew 200
Meena withdrew 1000'''

print("ATM Transaction System\n")

try:
    name = input("Enter customer name: ")
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be positive")
    with open("transactions.txt", "a") as file:
        file.write(f"{name} withdrew {amount}\n")
    print("Transaction successful")
except ValueError:
    print("Invalid amount entered")
except IOError:
    print("File error occurred")
except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Transaction process completed")

'''
Output:
ATM Transaction System

Enter customer name: Dharshini
Enter withdrawal amount: 8000
Transaction successful
Transaction process completed

transaction.txt

Dharshni, 8000
'''
