# 31. Next Permutation
nums = [1,2,3]

n = len(nums)

# Step 1: find position to change
i = n - 2
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