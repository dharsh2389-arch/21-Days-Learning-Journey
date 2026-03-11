'''
Create a program that analyzes a number entered by the user.
The program should:
Ask the user to enter a positive integer
Calculate the sum of all digits in the number
Display the largest digit in the number
Display the number of digits
Example
Copy code

Input:
Enter number: 4729
Output
Copy code

Sum of digits: 22
Largest digit: 9
Total digits: 4
'''

number = input("Enter number: ")
sum = 0
largest = 0
for i in number:
    d = int(i)
    sum += d
    if d > largest:
        largest = d
print("Sum of digits:", sum)
print("Largest digit:", largest)
print("Total digits:", len(number))

'''Output
Enter number: 1234
Sum of digits: 10
Largest digit: 4
Total digits: 4
'''
