'''Two strings are isomorphic if characters in one string can be replaced to get the other string'''

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) != len(s2):
    print("Not Isomorphic")
else:
    mapping = {}
    used = set()
    flag = True
    for i in range(len(s1)):
        if s1[i] in mapping:
            if mapping[s1[i]] != s2[i]:
                flag = False
                break
        else:
            if s2[i] in used:
                flag = False
                break
            mapping[s1[i]] = s2[i]
            used.add(s2[i])
    if flag:
        print("Isomorphic")
    else:
        print("Not Isomorphic")

  '''Output
  Enter first string: paper
Enter second string: title
Isomorphic
'''
