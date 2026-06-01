from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0 
            
        i = 0 
        n = len(nums)
        while i < n-1:
            if nums[i+1] != nums[i] + 1:
                return nums[i]+1
            i+=1    
        return len(nums)
    
solution = Solution()
print(solution.missingNumber([3,0,1]))

