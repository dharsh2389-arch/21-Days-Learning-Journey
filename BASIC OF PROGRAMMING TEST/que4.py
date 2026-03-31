amount=int(input("Enter amount: "))
location=input("Enter location(home or new): ")
time=input("Enter time(HH:MM): ")
failed_attempts=int(input("Enter number of failed attempts: "))
if failed_attempts>=3:
    print("Risk Level: LOCK")
else:
    risk=0
    if amount>50000:
        risk+=1
    if int(time[:2])>=0 and int(time[:2])<5:
        risk+=1
    if location=="new":
        risk+=1
    if risk>=2:
        print("Risk Level: HIGH")
    else:
        print("Risk Level: LOW")
