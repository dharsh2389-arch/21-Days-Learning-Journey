correct_username = "admin"
correct_password = "1234"
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong credentials")
        print("Attempts left:", attempts)
if attempts == 0:
    print("Account Locked")

'''
Output
Enter username: dharshini
Enter password: 2749590393
Wrong credentials
Attempts left: 2
Enter username: reena
Enter password: 29393002
Wrong credentials
Attempts left: 1
Enter username: admin
Enter password: 1234
Login Successful
'''
