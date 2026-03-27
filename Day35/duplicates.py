arr = [1, 2, 3, 2, 4, 5, 1]
s = set()
duplicates = set()
for num in arr:
    if num in s:
        duplicates.add(num)
    else:
        s.add(num)
print(list(duplicates))

'''
Output
[1, 2]
'''
