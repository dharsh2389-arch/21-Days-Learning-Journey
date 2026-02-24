'''Store marks of 5 subjects in a list and calculate:
Marks
Total
Average
Highest mark
Lowest marl'''

print("Student Mark Analyzer\n")
marks=[]
for i in range(1,6):
    mark=float(input("Enter the mark for subject " + str(i) + ":"))
    marks.append(mark)
total=sum(marks)
average=total/len(marks)
print("Marks: ",marks)
print("Total marks: ",total)
print("Average marks: ",average)
print("Highest mark: ",max(marks))
print("Lowest mark: ",min(marks))
