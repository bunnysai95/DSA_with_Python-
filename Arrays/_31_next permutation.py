# 31. Next Permutation
nums= [1,2,3]
nums = [1,3,5,4,2]
# output = [1,4,2,3,5]

n = len(nums)
print(n,"n_value")
# Step 1: find position to change
i = n - 2
print(i,"i_value")
while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1
# Step 2: if such position exists
if i >= 0:
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    # swap
    nums[i], nums[j] = nums[j], nums[i]
# Step 3: reverse the rest (simple way)
nums[i+1:] = nums[i+1:][::-1]
print(nums)

