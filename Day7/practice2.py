'''Question:
Design a Password Strength Checker.
Rules:
Minimum length 8
Must contain at least one uppercase letter
Must contain at least one lowercase letter
Must contain at least one digit
Must not contain spaces
Display:
Strong Password
Weak Password'''

print("Password Strength Checker\n")
password=input("Enter your password: ")
length=len(password)>=8
upper=0
lower=0
digit=0
space=0
for i in password:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
    if i.isdigit():
        digit+=1
    if i==" ":
        space+=1
        
if(length and upper>=1 and lower>=1 and digit>=1 and space==0):
    print("It is a Strong Password")
else:
    print("It is not a Strong Password")
