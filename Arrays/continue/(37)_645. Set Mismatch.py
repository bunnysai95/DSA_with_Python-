from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        seen = set()
        duplicate = -1 
        for num in nums:
            if num in seen:
                duplicate = num 
            seen.add(num)
        for i in range(1,len(nums)+1):
            if i not in seen : 
                missing = i 
                break
        return [duplicate, missing]

solution = Solution()
print(solution.findErrorNums([1,2,2,4]))
