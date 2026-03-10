'''Create a program to manage student attendance.
The program should allow the user to:
Add student name
Mark attendance as Present or Absent
Display all student attendance records
Example Output
Copy code
Student Attendance
Dharshini - Present
Rahul - Absent
Anu - Present'''

attendance = {}
while True:
    print("1 Add Student Attendance")
    print("2 Display Attendance")
    print("3 Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        pa = input("Enter whether Present/Absent: ")
        attendance[name] = pa
    elif choice == "2":
        print("Student Attendance")
        for name, pa in attendance.items():
            print(name, "-", pa)
    elif choice == "3":
        break

'''Output
1 Add Student Attendance
2 Display Attendance
3 Exit
Enter choice: 1
Enter student name: Dharshini
Enter whether Present/Absent: Present
1 Add Student Attendance
2 Display Attendance
3 Exit
Enter choice: 1
Enter student name: Reena
Enter whether Present/Absent: Absent
1 Add Student Attendance
2 Display Attendance
3 Exit
Enter choice: 2
Student Attendance
Dharshini - Present
Reena - Absent
1 Add Student Attendance
2 Display Attendance
3 Exit
Enter choice: 3
'''
