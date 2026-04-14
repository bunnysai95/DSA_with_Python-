nums = [1,0,-1,0,-2,2]
target = 0

'''loop through the listof arry 
sort the list
use two pointer approach to find the target sum
and keep condition to avoid duplicates
and append the result in new list and return the new list
and use while loop to move the left and right pointer to find the target sum
and also use while loop to avoid duplicates in the result list
'''
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        new_list = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1
                while l < r :
                    total=(nums[i]+nums[j]+nums[l]+nums[r])
                    if total < target:
                        l+=1
                    elif total>target:
                        r-=1
                    else:
                        new_list.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1 
                        r-=1
        return new_list
    
solution = Solution()
result = solution.fourSum(nums, target) 
print(result)
