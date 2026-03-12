'''Question Statement
Write a Python program to count the frequency of each character in a given string using a dictionary.
Example:
Input:
programming
Output:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}'''

text = input("Enter a string: ")

dict = {}
for i in text:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("Characters:", dict)
