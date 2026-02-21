'''Placement Eligibility System
Design a Placement Eligibility System for a company.
Take:
Name, 10th percentage, 12th percentage, Current CGPA, Number of standing arrears

Eligibility Rules:
If:
10th ≥ 70, 12th ≥ 70, CGPA ≥ 7.5, Arrears = 0
→ Eligible for Dream Company
If:
10th ≥ 60, 12th ≥ 60, CGPA ≥ 6.5, Arrears ≤ 1
→ Eligible for Core Company
If:
CGPA ≥ 6.0, Arrears ≤ 2
→ Eligible for Mass Recruiter
Otherwise → Not Eligible'''

print("Placement Eligibility System\n")
name=input("Enter your Name: ")
tenth = float(input("Enter 10th Mark in Percentage: "))
twelth = float(input("Enter 12th Mark in Percentage: "))
cgpa = float(input("Enter Current CGPA: "))
arrears = int(input("Enter Number of Arrears: "))

if(tenth >= 70 and twelth >= 70 and cgpa >= 7.5 and arrears == 0):
    print("Status: Eligible for Dream Company")
elif(tenth >= 60 and twelth >= 60 and cgpa >= 6.5 and arrears <= 1):
    print("Status: Eligible for Core Company")
elif(cgpa >= 6.0 and arrears <= 2):
    print("Status: Eligible for Mass Recruiter")
else:
    print("Status: Not Eligible")
