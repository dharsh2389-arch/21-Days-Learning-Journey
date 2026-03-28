import random
import string
length = int(input("Enter password length: "))
char = string.ascii_letters + string.digits + "!@#$%"
password = ""
for i in range(length):
    password += random.choice(char)
print("Generated Password:", password)

'''
Output 1
Enter password length: 8
Generated Password: W!Zzswl$

Output 2
Enter password length: 10
Generated Password: KPZN4Hz4b#
'''
