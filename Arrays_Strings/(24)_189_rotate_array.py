nums = [1,2,3,4,5,6,7]
k = 3
Output= [5,6,7,1,2,3,4]
#optimized solution
n = len(nums)
k %= n
nums.reverse()
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])

print(nums)


nums = [1,2,3,4,5,6,7]
k = 3
Output= [5,6,7,1,2,3,4]


i,m = 0,0 
j = len(nums)-1
k = k % n
# reversed whole arr
while i < j : 
    nums[i],nums[j] = nums[j], nums[i]
    i += 1
    j -=1
print(nums, "revered whole list")
# reverse list till point k 
i = 0 
j = k - 1
while i < j:
    nums[i],nums[j] = nums[j], nums[i]
    i +=1 
    j -=1
print(nums,"revered till kth index")
# step 3 reveresing rest of al the list 
i = 3 
j = len(nums)-1
while i < j :
    nums[i], nums[j] = nums[j], nums[i]
    i +=1
    j-=1
print(nums, "final result")
