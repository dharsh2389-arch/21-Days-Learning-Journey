nums=list(map(int, input("Enter numbers: ").split()))
key=int(input("Enter number to search: "))
ind=-1
for i in range(len(nums)):
    if nums[i]==key:
        ind=i
        break
print(ind)

'''
Output
Enter numbers: 3 94 204 2 45 43
Enter number to search: 204
2
'''
