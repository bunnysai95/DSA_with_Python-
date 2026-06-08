'''
724. Find Pivot Index
Input: nums = [1,7,3,6,5,6]
Output: 3
'''
nums = [1,7,3,6,5,6]

def pivotIndex(nums):
    total = 0 
    total = sum(nums)
    left = 0  # prefix sum

    for i in range(len(nums)):
        right = total - left - nums[i] 
        if left == right:
            return i
        left += nums[i]
    return (-1,"not found")
print(pivotIndex(nums))

'''
o(n), o(1)
prefix total
total -left - current element = (right == left) then return index 
'''