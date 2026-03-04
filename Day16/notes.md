Exception Handling (Python)
  Exception handling helps your program handle errors gracefully instead of crashing.

What is an Exception?
  An exception is an error that occurs during program execution.
  Example:
  a = 10
  b = 0
  print(a / b)

  #Output: ZeroDivisionError: division by zero

Why Use Exception Handling?
  -> Prevent program crash
  -> Handle user mistakes
  -> Improve program reliability
  -> Provide meaningful error messages

  It is used in:
  -> Login systems
  -> Payment systems
  -> File reading
  -> APIs

try – except concept:
  Syntax:
  try:
      risky_code
  except:
      handle_error

  Example:
  try:
      num = int(input("Enter number: "))
      result = 100 / num
      print(result)
  except:
      print("An error occurred")

  #If user enters 0 or text, program will not crash.

Catching Specific Exceptions:
  Example:
  try:
    num=int(input("Enter number: "))
    result=100/num
    print(result)
  except ZeroDivisionError:
    print("You cannot divide by zero")
  except ValueError:
    print("Invalid Input")

try-except-else concept:
  else runs when no exception occurs.
  Example:
  try:
    num=int(input("Enter number: "))
    result=100/num
  except ZeroDivisionError:
    print("You cannot divide by zero")
  else:
    print("Result",result)

try-except-finally concept:
  finally always runs.
  Example:
  try:
    file=open("data.txt","r")
  except FileNotFoundError:
    print("File Not Found")
  finally:
    print("Execution finished")

  #even if error occurs, finally runs.

Raising Exceptions
  You can manually raise errors.
  Example:
  age = int(input("Enter age: "))
  if age < 18:
    raise ValueError("Age must be 18 or above")
    print("Eligible")

Common Python Exceptions:

  Exception	         Cause
  ValueError	       Invalid value
  TypeError	         Wrong data type
  ZeroDivisionError	 Divide by zero
  FileNotFoundError	 File missing
  IndexError	       Invalid list index
  KeyError	         Invalid dictionary key
