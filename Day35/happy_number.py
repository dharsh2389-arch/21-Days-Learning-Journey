'''
A number is called a happy number if:
->Replace the number by the sum of squares of its digits
->Repeat the process
->If it becomes 1 → Happy number
->If it loops endlessly → Not happy
'''

def happy(n):
    s = set()
    while n != 1 and n not in s:
        s.add(n)        
        n = sum(int(digit)**2 for digit in str(n))    
    return n == 1
num = int(input("Enter a number: "))
if happy(num):
    print("Happy Number")
else:
    print("Not Happy Number")

'''
Output 1
Enter a number: 19
Happy Number

Output 2
Enter a number: 25
Not Happy Number
'''
