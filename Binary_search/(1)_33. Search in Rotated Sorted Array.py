from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, val in enumerate(nums):
            if val == target:
                return i 
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
call = Solution()
result = call.search(nums,target)
print(result)

'''
linear search
log(n), o(1)
'''




