File Handling:

What is File Handling?
  When a program ends, data disappears. 
  File handling allows you to:
  i. Store data permanently 
  iii. Modify stored data

  File Handling is used in:
  i. Login System
  ii. Bank system
  iii. Student records
  iv. Billing Systems

Opening a file:
  Syntax: 
  file = open("filename.txt", "mode")

  File modes:
  Mode   Meaning
  "r"    Read file
  "w"    Write (overwrite file)
  "a"    Append (add data)
  "x"    Create new file

Writing to File:
  Example:
  file = open("data.txt","w")
  file.write("Hello Python")
  file.write("Learning File Handling\n")
  file.close()

Reading from file:
  file=open("data.txt","r")
  content=file.read()
  print(content)
  file.close()

Append Mode:
  file=open("data.txt","a")
  file.write("This is appended line")
  file.close()

Instead of manually closing, we can also write
  with open("data.txt","r") as file:
    content = file.read()
    print(content)

Reading Line by Line 
  with open("data.txt","r") as file:
    print(file.readline())

Using realines()
  with open("data.txt","r") as file:
    lines=file.readlines()
    print(lines)
