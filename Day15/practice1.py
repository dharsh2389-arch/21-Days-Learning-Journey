'''Question:
1. Add student
2. Store name + marks
3. Display all students
4. Calculate Average'''

print("Student Record System")
while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice=input("Enter choice: ")
    if choice=="1":
        name=input("Enter name: ")
        marks=input("Enter marks: ")
        with open("student.txt", "a") as file:
            file.write(name +","+ marks + "\n")
        print("Student added successfully")
    elif choice=="2":
        total=0
        count=0
        with open("student.txt","r") as file:
            for line in file:
                name, marks=line.strip().split(",")
                print("Name:", name, "Marks:", marks)
                total+=float(marks)
                count+=1
        if count>0:
            print("Average marks:", total/count)
    elif choice =="3":
        break
    else:
        print("Invalid choice")

'''
Output:
Student Record System
1. Add Student
2. View Student
3. Exit
Enter choice: 1
Enter name: Dharshini
Enter marks: 98
Student added successfully
1. Add Student
2. View Student
3. Exit
Enter choice: 1
Enter name: Sumitha
Enter marks: 99
Student added successfully
1. Add Student
2. View Student
3. Exit
Enter choice: 1
Enter name: Divya
Enter marks: 96
Student added successfully
1. Add Student
2. View Student
3. Exit
Enter choice: 2
Name: Dharshini Marks: 98
Name: Sumitha Marks: 99
Name: Divya Marks: 96
Average marks: 97.66666666666667
1. Add Student
2. View Student
3. Exit
Enter choice: 3
  
student.txt

Dharshini,98
Sumitha,99
Divya,96
'''
