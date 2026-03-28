sentence = input("Enter a sentence: ").lower()
words = sentence.split()
vowels = "aeiou"
v_count = 0
c_count = 0
for i in sentence:
    if i.isalpha():
        if i in vowels:
            v_count += 1
        else:
            c_count += 1
print("Words:", len(words))
print("Vowels:", v_count)
print("Consonants:", c_count)

'''
Output
Enter a sentence: Python is the simplest programming language
Words: 6
Vowels: 12
Consonants: 26
'''
