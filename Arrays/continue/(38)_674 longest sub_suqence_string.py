# 674. Longest Continuous Increasing Subsequence

from typing import List 

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i =0 
        count = 1
        max_count = 1
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                count +=1 
            else: 
                count = 1
            max_count = max(count, max_count) 
            i +=1 
        
        return max_count 


print(Solution().findLengthOfLCIS([1,3,5,4,7]))