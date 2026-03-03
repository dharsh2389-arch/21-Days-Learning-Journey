'''Question
1. Add daily expense
2. Store in file
3. Calculate total expense
4. Show highest expense'''

print("Expense Tracker")
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")
    choice=input("Enter choice: ")
    if choice =="1":
        amount=input("Enter your expense: ")
        with open("expense.txt","a") as file:
            file.write(amount + "\n")
        print("Expense recorded")
    elif choice =="2":
        total =0
        highest=0
        with open("expense.txt","r") as file:
            for line in file:
                amount=float(line.strip())
                total+=amount
                if amount>highest:
                    highest=amount
        print("Total Expense: ", total)
        print("Highest Expense: ",highest)
    elif choice == "3":
        break
    else:
        print("Invalid choice")

  '''
  Output:
  Expense Tracker
1. Add Expense
2. View Expense
3. Exit
Enter choice: 1
Enter your expense: 8000
Expense recorded
1. Add Expense
2. View Expense
3. Exit
Enter choice: 1
Enter your expense: 4500
Expense recorded
1. Add Expense
2. View Expense
3. Exit
Enter choice: 2
Total Expense:  12500.0
Highest Expense:  8000.0
1. Add Expense
2. View Expense
3. Exit
Enter choice: 3

expense.txt
8000
4500
'''
