'''Question
Create a contact book where the user can:
Add contact
Search contact
Display contacts
Store data using a dictionarys'''

contacts = {}
while True:
    print("1 Add Contact")
    print("2 Search Contact")
    print("3 Display Contacts")
    print("4 Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Not found"))
    elif choice == "3":
        print(contacts)
    elif choice == "4":
        break

'''
Output
1 Add Contact
2 Search Contact
3 Display Contacts
4 Exit
Enter choice: 1
Enter name: Dharshini
Enter phone: 9876543210
1 Add Contact
2 Search Contact
3 Display Contacts
4 Exit
Enter choice: 1
Enter name: Reena
Enter phone: 9753108642
1 Add Contact
2 Search Contact
3 Display Contacts
4 Exit
Enter choice: 2
Enter name to search: Dharshini
9876543210
1 Add Contact
2 Search Contact
3 Display Contacts
4 Exit
Enter choice: 2
Enter name to search: Meena
Not found
1 Add Contact
2 Search Contact
3 Display Contacts
4 Exit
Enter choice: 3
{'Dharshini': '9876543210', 'Reena': '9753108642'}
1 Add Contact
2 Search Contact
3 Display Contacts
4 Exit
Enter choice: 4
'''
