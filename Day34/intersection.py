def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
print("Intersection: ",intersection([1,2,2,1], [2,2]))

'''Output
Intersection:  [2]
'''
