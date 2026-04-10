# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Brute Force 

# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6
result = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==target:
            result.append([i,j])
print(result)
# Time Complexity: O(n^2)
# Space Complexity: O(1)    

# Optimal Solution
from ast import List
from typing import List
nums = [2,7,11,15]   
target = 9
def twoSum(self, nums: List[int], target: int) -> List[int] | None:
    empty = {}
    for i, num in enumerate(nums):
        _list_1 = target - num 
        if _list_1 in empty: 
            return  [empty[_list_1], i]
        empty[num] = i 

print(twoSum(1, nums, target))