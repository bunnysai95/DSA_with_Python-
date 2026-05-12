nums = [1,3,2,2,5,2,3,7]
output = 5
import collections
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        count_values = collections.Counter(nums)
        max_length = 0 
        for i in count_values:
            if i + 1 in count_values:
                current_length = count_values[i] + count_values[i+1]
                if current_length > max_length:
                    max_length = current_length 
        return max_length
result = Solution()
print(result.findLHS(nums))
"""
logic finding nums(n , n+1) with difference 1 
checking if there is n , and n+1 in array then
counting frequency of n & n+1  in array if max_leng is > len(nums) return max_length
"""