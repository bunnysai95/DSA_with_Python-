nums = [5,7,7,8,8,10]
target = 8

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        n = len(nums)
        if not nums:
            return [-1,-1]
        l = 0 
        r = n-1 
        # left binary search 
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target: r = mid - 1 
            else: l = mid + 1
        if l < n and nums[l] == target: start = l
        # right binary search 
        l, r = 0, n-1
        while l <= r :
            mid = (l+r)//2
            if nums[mid] <= target : l = mid+1
            else: r = mid -1
        # if nums[r-1] == target: end = r-1 
        if r >= 0 and nums[r] == target:
            end = r
        return [start, end]
    
solution = Solution()
result = solution.searchRange(nums, target)
print(result)
