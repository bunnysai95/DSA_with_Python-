'''
1480. Running Sum of 1d Array
'''

nums = [1,2,3,4]
Output= [1,3,6,10]
new_s  = []
sum = 0 
for i in range(len(nums)):
    sum += nums[i]   
    new_s.append(sum)
print(new_s)

# optimized solution
'''
using acclumation 
'''
from itertools import accumulate
print(list(accumulate(nums)))