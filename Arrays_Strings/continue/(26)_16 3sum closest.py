
nums = [-1,2,1,-4]
target = 1
nums.sort()
n = len(nums)
closest  = nums[0]+nums[1]+nums[2]
for i in range(n-2):
    l = i + 1 
    r = n - 1
    while l < r: 
        current = nums[i]+nums[l]+nums[r]
        if abs(current- target) < abs(closest-target):        
            closest = current
        if current < target:
            l +=1 
        elif current > target:
            r -=1 
        else:
            print(current)
print(closest)