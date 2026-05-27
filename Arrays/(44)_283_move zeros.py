nums = [0,1,0,3,12]

i = 0 
j = 0
while j < len(nums):
    if j == 0 :
        nums[i] = nums[j]
        j += 1 
        i +=1 
    else:
        j += 1
while i < len(nums): 
    nums[i] = 0 
    i += 1 

print(nums)

