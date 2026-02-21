'''Scholarship Eligibility Analyzer
Design a Scholarship Eligibility Analyzer using conditional statements.
Take:
Student marks in percentage
Family annual income
Category (general / obc / sc / st)

Scholarship Rules:
If marks ≥ 90 and income ≤ 3,00,000 → Full Scholarship
If marks ≥ 75 and income ≤ 5,00,000 → 50% Scholarship
If category is sc or st and marks ≥ 60 → Special Category Scholarship
Otherwise → Not Eligible
Display the scholarship status.'''

print("Scholarship Eligibility Analyzer")
marks = float(input("Enter student's marks in percentage: "))
income = float(input("Enter Family's Annual income: "))
category = input("Enter Category (general/obc/sc/st): ")

if marks >= 90 and income <= 300000:
    print("Status: Full Scholarship")
elif marks >= 75 and income <= 500000:
    print("Status: 50% Scholarship")
elif (category == "sc" or category == "st") and marks >= 60:
    print("Status: Special Category Scholarship")
else:
    print("Status: Not Eligible")
