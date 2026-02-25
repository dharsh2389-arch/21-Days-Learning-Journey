'''Question
Find the second largest number in a list.'''

num=[10,70,30,40,10,60,40]
x=list(set(num))
x.sort()
print("Second Largest Number Is: ",x[-2])
