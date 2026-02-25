'''Store student records as tuples (Roll No, Name, Department)
Store course enrollment using sets
Remove duplicate enrollments
Find students enrolled in both courses
Display total unique students'''

print("College Course Enrollment System\n")
s1 = (101, "Dharshini", "ECE")
s2 = (102, "Reena", "CSE")
s3 = (103, "Meena", "IT")
students = [s1, s2, s3]
print("Student Records:")
for s in students:
    print(s)
python = {"Dharshini", "Meena", "Reena","Dharshini"}
java = {"Dharshini", "Meena"}
print("Python Course Students:", python)
print("Java Course Students:", java)
common = python.intersection(java)
print("Students in Both Courses:", common)
all = python.union(java)
print("Total Unique Enrolled Students:", len(all))
