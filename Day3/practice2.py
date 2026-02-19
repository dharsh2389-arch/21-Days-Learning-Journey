#BMI Calculator

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
#Formula for BMI = weight/(height^2)
bmi = weight / (height * height)
print("Your BMI is:", round(bmi, 2))

'''Types used in BMI Calculator is:
1. float - to convert height and weight into a decimal number because BMI will be in decimal number
2. input() - for getting input as a string '''

#Simple Interest Calculator 

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
#Formula for Simple Interest = (principal x rate x time)/100
interest = (principal * rate * time) / 100
print("Simple Interest is:", interest)

'''Types used in Simple Interest Calculator is:
1. input() - getting input as a string 
2. float - converting the input string into a decimal number because interest will be in decimal value
