'''
loop till last
use hashmap to store the last index of each element
if nums seen in hashmap 
and index difference is less than or equal to k return true
else update the index of the element in hashmap
'''

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen ={}
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False
solution = Solution()
nums = [1,2,3,1]
k = 3
result = solution.containsNearbyDuplicate(nums, k)
print(result)
