total_messages=int(input("Enter total number of messages: "))
status=""
active=0
compressed=0
if total_messages<=100:
    status="Normal"
    active=total_messages
    compressed=0
else:
    status="Optimized"
    active=100
    compressed=total_messages-active
print("Status: ",status," Active: ",active," Compressed: ",compressed)
