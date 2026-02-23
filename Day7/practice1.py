'''Question:
Design an Email Validation System.
Rules:
Email must contain '@'
Email must contain '.'
'@' must come before '.'
No spaces allowed
Email must be at least 6 characters long
Display whether the email is valid or invalid.'''

print("Email Validator System\n")
email=input("Enter your email id: ")
length=len(email)>=6
at="@" in email
dot="." in email
space=" " in email
at_pos= email.find("@")
dot_pos=email.find(".")
pos=at_pos<dot_pos
if length and at and dot and not space and pos:
    print("Email is valid")
    print("Email:",email)
else:
    print("Email is not valid")
