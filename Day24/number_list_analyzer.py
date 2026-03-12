'''Create a program that works with a list of numbers.
The program should:
Ask the user to enter 5 numbers
Store them in a list
Display:
Sum of numbers
Largest number
Smallest number
Example
Input:
10 20 5 8 12
Output:
Sum: 55
Largest: 20
Smallest: 5'''

number = []
for i in range(5):
    num = int(input("Enter number: "))
    number.append(num)
print("Sum:", sum(number))
print("Largest:", max(number))
print("Smallest:", min(number))

'''Output
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Sum: 15
Largest: 5
Smallest: 1
'''
