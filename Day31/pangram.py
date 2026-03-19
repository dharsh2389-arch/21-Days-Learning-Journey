'''
A pangram is a sentence that contains all 26 alphabets (a–z) at least once.
'''

text = input("Enter sentence: ").lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
for char in alphabets:
    if char not in text:
        print("Not Pangram")
        break
else:
    print("Pangram")

'''Output
Enter sentence: The quick brown fox jumps over the lazy dog
Pangram
'''
