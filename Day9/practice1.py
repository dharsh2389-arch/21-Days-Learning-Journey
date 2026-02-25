'''Question
Given a list of numbers, print:
Unique elements (appearing once)
Repeated elements (appearing more than once)'''

num=[1,2,2,6,3,4,6,7,8]
unique=[]
repeat=set()
for i in num:
    if num.count(i)==1:
        unique.append(i)
    else:
        repeat.add(i)
        
print("Unique numbers: ",unique)
print("Repeated numbers: ",repeat)
