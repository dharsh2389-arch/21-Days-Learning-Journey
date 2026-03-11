'''Create a program that analyzes a sentence entered by the user.
The program should:
Take a sentence from the user
Split it into words
Store each word and its length in a dictionary
Display the word lengths
Example
Copy code

Input:
Python is powerful

Output:
Python : 6
is : 2
powerful : 8'''

sentence = input("Enter a sentence: ")
words = sentence.split()
word_length = {}
for word in words:
    word_length[word] = len(word)
print("Word Lengths:")
for word, length in word_length.items():
    print(word, "-", length)

'''Output
Enter a sentence: Python is a language
Word Lengths:
Python - 6
is - 2
a - 1
language - 8
'''
