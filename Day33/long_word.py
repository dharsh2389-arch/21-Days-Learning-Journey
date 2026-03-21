sentence = input("Enter sentence: ")
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

'''Output
Enter sentence: Python is a easiest programming language
Longest word: programming
'''
