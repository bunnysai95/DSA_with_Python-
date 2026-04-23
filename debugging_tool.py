nums = [0,0,1,1,1,1,2,3,3]
output = 7 

ptr , count = 0 , 1 
for i in range(1, len(nums)):
    if nums[ptr] == nums[i] and count<2:
        ptr += 1 
        count += 1 
        nums[ptr],nums[i] = nums[i], nums[ptr]
    elif nums[ptr] != nums[i]:
        ptr += 1
        count = 1 
        nums[ptr],nums[i] = nums[i],nums[ptr]

print(ptr+1)