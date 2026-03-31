request_count=int(input("Enter number of API calls made: "))
status=""
if request_count<=5:
    status="Allowed"
else:
    status="Booked(Rate Limit Exceeded)"
print("Status: ",status)
