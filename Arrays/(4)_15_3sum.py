class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        new_nums = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1 
            right = len(nums)-1
            while left < right :
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    new_nums.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0 :
                    left += 1
                else: 
                    right -=1
        return new_nums
solution = Solution()
nums = [-1,0,1,2,-1,-4]
result = solution.threeSum(nums)
print(result)
# [[-1, -1, 2], [-1, 0, 1]]

# core logic
nums = [-1,0,1,2,-1,-4]
nums.sort()
new_list = []
for i in range(len(nums)):
    left = i+1 
    right = len(nums)-1
    while left < right:
        if nums[i]+nums[left]+nums[right] == 0 :
            new_list.append([nums[i],nums[left],nums[right]])
        left+=1 
        right-=1
print(new_list)

'''two pointer approch'''