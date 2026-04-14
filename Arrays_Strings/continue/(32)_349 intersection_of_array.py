from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        return list(set_1.intersection(set_2))
    
solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
result = solution.intersection(nums1, nums2)
print(result)
