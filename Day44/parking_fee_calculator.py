'''
Question:
Calculate parking fee based on hours parked:
Rules:
First 2 hours → ₹10 per hour
Next 3 hours → ₹20 per hour
Above 5 hours → ₹30 per hour
'''

hours=int(input("Enter parking hours: "))
fee=0
if hours<=2:
    fee=hours*10
elif hours<=5:
    fee=(2 * 10)+(hours - 2)*20
else:
    fee=(2 * 10)+(3 * 20)+(hours - 5)*30
print("Total parking fee: ₹",fee)

'''
Output
Enter parking hours: 7
Total parking fee: ₹ 140
'''
