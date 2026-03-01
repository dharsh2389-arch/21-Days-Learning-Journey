'''Create a class Student.
Attributes:
name
marks
Methods:
calculate_grade()
display()
Grade logic:
≥ 90 → A
≥ 75 → B
≥ 50 → C
else → Fail
Create 3 students and display results.'''

class Student:
  def __init__(self,name,mark):
    self.name=name
    self.mark=mark
  def calculate_grade(self):
    if self.mark>=90:
      return "Grade A"
    elif self.mark>=75 and self.mark<90:
      return "Grade B"
    elif self.mark>=50 and self.mark<75:
      return "Grade C"
    else:
      return "Fail"
  def display(self):
    print(self.name,self.calculate_grade())
s1=Student("Dharshini",63)
s2=Student("Sumitha",76)
s3=Student("Gayathri",55)
s1.display()
s2.display()
s3.display()

'''Output
Dharshini Grade C
Sumitha Grade B
Gayathri Grade C'''
