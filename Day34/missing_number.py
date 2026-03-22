def missing_number(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)

    return expected - actual
print("Missing numbers: ",missing_number([3,0,1]))

'''Output
Missing numbers:  2
'''
