'''Question:
Design a Student Database Management System.
Create an empty student list.
Add student names.
Insert a transfer student at a specific position.
Remove a discontinued student.
Remove last admitted student.
Display:
Total number of students
First and last student
Sort student names alphabetically.
Reverse the student list.
Clear the entire database.'''

print("Student Database Management System\n")
students = []
students.append("Dharshini")
students.append("Reena")
students.append("Meena")
students.append("Teena")
print("Students:",students)
students.insert(2, "Priya")
print("After Inserting Transfer Student:",students)
students.remove("Meena")
print("After Removing Discontinued Student:",students)
students.pop()
print("After Removing Last Student:",students)
print("Total Students:",len(students))
print("First Student:",students[0])
print("Last Student:",students[-1])
students.sort()
print("Sorted Student List:", students)
students.reverse()
print("Reversed Student List:", students)
students.clear()
print("Student Database After Clear:", students)
