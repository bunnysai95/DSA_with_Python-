nums = [1,2,3,1]
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        new_list = set()
        for i in range(len(nums)):
            if nums[i] in new_list:
                return True
            else:
                new_list.add(nums[i])
        return False
    
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)