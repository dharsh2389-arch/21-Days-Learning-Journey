try:
    with open("students.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File does not exist")
finally:
    print("File operation finished")

'''
Output:
File does not exist
File operation finished
'''
