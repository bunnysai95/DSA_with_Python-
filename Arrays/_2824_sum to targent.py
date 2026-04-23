from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j  = 0, len(nums)-1 
        count =0 
        while i < j:
            if nums[i] + nums[j] < target:
                count+=(j-i) 
                i +=1 
            else:
                j -=1
        return count

solution = Solution()
nums = [1,2,3,4,5]
nums = [1,1,1,3]
nums = [1,1,2,2]
target = 4
result = solution.countPairs(nums, target)
print(result)
