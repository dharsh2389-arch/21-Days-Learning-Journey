'''Questio
A teacher has a list of student marks.
Build a program that:
Filters students who passed (≥ 50).
Adds 5 grace marks to all students.
Finds students scoring ≥ 75.
Displays student names with marks.
Data:
Names: ["Ram","Sam","John","Priya","Anu"]
Marks: [45,78,90,56,32]'''

names = ["Ram","Sam","John","Priya","Anu"]
marks = [45,78,90,56,32]
passed = [m for m in marks if m >= 50]
grace_marks = list(map(lambda x: x + 5, marks))
high_scores = list(filter(lambda x: x >= 75, marks))
student_data = dict(zip(names, marks))
print("Passed:", passed)
print("Grace Marks:", grace_marks)
print("High Scores:", high_scores)
print("Student Data:", student_data)

'''Output
Passed: [78, 90, 56]
Grace Marks: [50, 83, 95, 61, 37]
High Scores: [78, 90]
Student Data: {'Ram': 45, 'Sam': 78, 'John': 90, 'Priya': 56, 'Anu': 32}
'''
