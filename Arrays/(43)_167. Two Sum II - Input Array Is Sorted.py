
'''
167. Two Sum II - Input Array Is Sorted
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Given a 1-indexed array of integers numbers that
is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0 
        r = n-1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target :
                return ([l+1, r+1])
            elif sum < target: l +=1 
            else: r -=1 
        return []
    
numbers = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(numbers, target)
print(result)

'''
    initilizing l, r moving inwards 
    if sum of them == target return the index + 1
    if sum < target move l pointer to right 
    else move r pointer to left
    if we exit the loop without finding a solution return empty list
    time complexity O(n) and space complexity O(1)
'''