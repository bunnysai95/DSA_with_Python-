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

nums = [5,7,7,8,8,10]
target = 8
Output= [3,4]
start,end  = -1, -1

if not nums:
    print([-1,-1])
n = len(nums)
l = 0 
r = n-1
# binary left search
while l < r:
    mid = (l + r) // 2
    if nums[mid] >= target:
        r = mid
    else:
        l = mid+1
if l < n and nums[l] == target: start = l
# right search
l , r  = 0, n
while l < r:
    mid = (l+r) //2
    if nums[mid] <= target:
        l = mid+1
    else:
        r=mid
if nums[r-1] == target: end = r-1
print(start, end)