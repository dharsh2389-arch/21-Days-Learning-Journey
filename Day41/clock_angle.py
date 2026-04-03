hour=int(input("Enter hour: "))
minute=int(input("Enter minutes: "))
hour=hour%12
hour_angle=(hour*30)+(minute*0.5)
minute_angle=minute*6
angle=abs(hour_angle-minute_angle)
angle=min(angle,360-angle)
print("Angle:",angle)

'''
Output
Enter hour: 5
Enter minutes: 20
Angle: 40.0
'''
