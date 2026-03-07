'''Question
Create a program that performs a countdown timer using recursion.
The user enters a number, and the program counts down to 0.
Example
Input: 5
Output:
5
4
3
2
1
0'''

def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n-1)

num = int(input("Enter countdown number: "))
countdown(num)

'''
Output
Enter countdown number: 10
10
9
8
7
6
5
4
3
2
1
0
'''
