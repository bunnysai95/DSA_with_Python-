from typing import List
class NumArray:
    '''
    [-2,0,3,-5,2,-1] prefixed sum [-2,-2+0=-2, -2+3=1, 1-5=-4, -4+2=-2, -2-1=-3]
    in init we are prefixing suming all the values with respesition to its previous value
    next --> funtion , reading right and left index
    sum = right - left will give us the sum of values in between  
    []'''


    def __init__(self, nums: List[int]):
        self.prefix =[]
        current = 0 
        for i in nums:
            current += i
            self.prefix.append(current)

    def sumRange(self, left: int, right: int) -> int:
        rightSum  = self.prefix[right]
        leftSum = self.prefix[left-1] if left > 0 else 0  
        return rightSum - leftSum

nums = [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]]
sums = NumArray(nums[0])
result = sums.sumRange(0, 5)    
print(result)

# output["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
