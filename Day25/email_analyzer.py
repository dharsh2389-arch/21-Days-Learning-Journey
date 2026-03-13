'''Write a program that analyzes an email entered by the user.
The program should:
Take an email as input
Extract the username
Extract the domain name
Example
Input:
dharshini@gmail.com
Output:
Username: dharshini
Domain: gmail.com'''

email = input("Enter email: ")
username, domain = email.split("@")
print("Username:", username)
print("Domain:", domain)

'''
Output
Enter email: dharsh2389@gmail.com 
Username: dharsh2389
Domain: gmail.com'''
