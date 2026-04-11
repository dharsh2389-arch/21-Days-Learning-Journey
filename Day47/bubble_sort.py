arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)

'''
Output
Enter numbers separated by spaces: 5 2 0 4 3
[0, 2, 3, 4, 5]
'''
