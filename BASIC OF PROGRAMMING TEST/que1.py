credit_score=int(input("Enter your credit score: "))
income=int(input("Enter your income: "))
emi=int(input("Enter EMI: "))
employment=input("Enter employment type: ")
status=""
interest_rate=""
if credit_score<600:
    status="Rejected"
    credit_score="N/A"
elif credit_score>=600 and credit_score<=749:
    status="Manual Review"
    interest_rate="N/A"
else:
    if income<25000:
        status="Rejected"
        interest_rate="N/A"
    elif emi>((50/100)*income):
        status="Rejected"
        interest_rate="N/A"
    elif employment not in ["Salaried", "Self Employed"]:
        status="Rejected"
        interest_rate="N/A"
    else:
        status="Approved"
        if credit_score>800:
            interest_rate="7%"
        else:
            interest_rate="8%"
print("Status: ",status)
print("Interest rate: ",interest_rate)
