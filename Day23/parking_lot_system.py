'''Create a program to manage a parking lot system.
The program should:
Allow vehicles to enter the parking lot
Store vehicle numbers in a list
Allow vehicles to exit the parking lot
Display all vehicles currently parked
Example Output
Copy code

1 Vehicle Entry
2 Vehicle Exit
3 Show Parked Vehicles
4 Exit

Enter choice: 1
Enter vehicle number: TN09AB1234
Vehicle parked'''

parking = []
while True:
    print("1 Vehicle Entry")
    print("2 Vehicle Exit")
    print("3 Show Parked Vehicles")
    print("4 Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        vehicle = input("Enter vehicle number: ")
        parking.append(vehicle)
        print("Vehicle parked")
    elif choice == "2":
        vehicle = input("Enter vehicle number to exit: ")
        if vehicle in parking:
            parking.remove(vehicle)
            print("Vehicle exited")
        else:
            print("Vehicle not found")
    elif choice == "3":
        print("Parked Vehicles:")
        for i in parking:
            print(i)
    elif choice == "4":
        break

'''Output
1 Vehicle Entry
2 Vehicle Exit
3 Show Parked Vehicles
4 Exit
Enter choice: 1
Enter vehicle number: 5678
Vehicle parked
1 Vehicle Entry
2 Vehicle Exit
3 Show Parked Vehicles
4 Exit
Enter choice: 1
Enter vehicle number: 2384
Vehicle parked
1 Vehicle Entry
2 Vehicle Exit
3 Show Parked Vehicles
4 Exit
Enter choice: 2
Enter vehicle number to exit: 5678
Vehicle exited
1 Vehicle Entry
2 Vehicle Exit
3 Show Parked Vehicles
4 Exit
Enter choice: 3
Parked Vehicles:
2384
1 Vehicle Entry
2 Vehicle Exit
3 Show Parked Vehicles
4 Exit
Enter choice: 4
'''
