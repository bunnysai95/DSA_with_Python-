
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1 
        current_area = 0 
        while left < right: 
            min_h = min(height[left], height[right])
            current_area = max((min_h*(right-left)),current_area)
            if height[left] < height[right]: 
                left +=1 
            else: right -=1
        return current_area
s = Solution()
height = [1,8,6,2,5,4,8,3,7]
result = s.maxArea(height)
print(result)   