numbers = [2, 7, 11, 15]
target = int(input("Enter target: "))
found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], "+", numbers[j], "=", target)
            found = True
if not found:
    print("No pair found")

'''Output
Enter target: 9
2 + 7 = 9
'''
