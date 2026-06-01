from typing import List 
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for current in arr:
            if current * 2 in seen or current / 2 in seen:
                return True
            seen.add(current)
        return False 
arr = [10,2,5,3]
solution = Solution()
result = solution.checkIfExist(arr)
print(result)