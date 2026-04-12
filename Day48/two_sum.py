def twoSum(nums,target):
    seen={}
    for i in range(len(nums)):
        comp=target-nums[i]
        if comp in seen:
            return [seen[comp],i]
        seen[nums[i]] = i
nums=list(map(int, input("Enter numbers: ").split()))
target=int(input("Enter target: "))
print(twoSum(nums,target))

'''
Output
Enter numbers: 2 5 7 11
Enter target: 9
[0, 2]
'''
