'''Create a program that analyzes a word entered by the user.
The program should:
Ask the user to enter a word or sentence
Count the number of vowels in the text
Display the total vowel count
Example
Input:
Enter text: python programming
Output:
Number of vowels: 4'''

text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0
for i in text:
    if i in vowels:
        count += 1
print("Number of vowels:", count)

'''
Output:
Enter text: I am Learning python
Number of vowels: 6
'''
