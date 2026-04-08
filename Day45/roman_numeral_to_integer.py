roman=input("Enter Roman numeral: ").upper()
values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total=0
for i in range(len(roman)):
    if i<len(roman)-1 and values[roman[i]]<values[roman[i+1]]:
        total-=values[roman[i]]
    else:
        total+=values[roman[i]]
print("Integer value:",total)

'''
Output
Enter Roman numeral: vi
Integer value: 6
'''
