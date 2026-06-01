
from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    missing = []
    nums_set = set(nums)
    for i in range(1, len(nums)+1):
        if i not in nums_set:
            missing.append(i)

    return missing

result = findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(result)
