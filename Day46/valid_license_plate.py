plate=input("Enter license plate: ")
if (len(plate)==10 and
    plate[:2].isalpha() and plate[:2].isupper() and
    plate[2:4].isdigit() and
    plate[4:6].isalpha() and plate[4:6].isupper() and
    plate[6:].isdigit()):
    print("Valid License Plate")
else:
    print("Invalid License Plate")

'''
Output 1
Enter license plate: TN74AB1234
Valid License Plate

Output 2
Enter license plate: TN74ABPO67
Invalid License Plate
'''
