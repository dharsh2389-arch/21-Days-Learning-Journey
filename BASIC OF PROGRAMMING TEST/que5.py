str = eval(input("Enter INFOR OR ERROR: "))
total=0
max=0
current=0
for i in str:
    if i=="ERROR":
        total+=1
        current+=1
        if current>max:
            max=current
    else:
        current=0
print("Total Errors:",total,", Longest Streak:",max)
