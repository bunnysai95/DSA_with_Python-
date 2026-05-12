nums = [1,12,-5,-6,50,3]
k = 4


# i = 0 
# j = len(nums)-3
# max_value = 0 
# while i < j :
#     total = (nums[i]+nums[i+1]+nums[i+2]+nums[i+3])/4
#     max_value = max(total, max_value)
#     i +=1
#     # j -=1 

# print(max_value)

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k,len(nums)):
    window_sum = window_sum + nums[i] - nums[i-k]   # this is thekey to this soultion 
    max_sum = max(max_sum, window_sum)

print(max_sum/k)

