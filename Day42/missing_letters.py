s = input("Enter a sentence: ").lower()
letters = "abcdefghijklmnopqrstuvwxyz"
missing = ""
for i in letters:
    if i not in s:
        missing += i
print("Missing letters:", missing)

'''
Output
Enter a sentence: Hello World
Missing letters: abcfgijkmnpqstuvxyz
'''
