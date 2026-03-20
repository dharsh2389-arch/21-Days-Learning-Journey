text = input("Enter string: ")
result = ""
count = 1
for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1
print("Compressed string:", result)

'''
Output
Enter string: aaaabbbbbbbbbccccccc
Compressed string: a4b9c7
'''
