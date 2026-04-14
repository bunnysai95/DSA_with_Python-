from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_uni = list(set(nums))
        nums_uni.sort()
        if len(nums_uni) < 3 : 
            return nums_uni[-1]

        return nums_uni[-3]
    
solution = Solution()
nums = [3,2,1]
result = solution.thirdMax(nums)
print(result)
