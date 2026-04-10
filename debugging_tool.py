# strs = ["aba","cdc","eae"]
# Output=  3


# def is_subseq(a, b):
#     i = 0
#     for ch in b:
#         if i < len(a) and a[i] == ch:
#             i += 1
#     return i == len(a)

# for i in range(len(strs)):
#     is_valid = True
#     for j in range(len(strs)):
#         if i != j and is_subseq(strs[i], strs[j]):
#             is_valid = False
#             break

# print(is_valid)


# -----------------------------------------------------------------------

nums = [1,0,-1,0,-2,2]
target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

for i in range(len(nums)-3):
    for j in range(i+1, len(nums)-2):
        left = j + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[j] + nums[left] + nums[right]
            if total == target:
                print([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1


