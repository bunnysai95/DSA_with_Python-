class Solution:
    def addDigits(self, num: int) -> int:
        value = num 
        while value > 9:
            count = 0
            while value !=0:
                unit_value = value % 10 
                count = unit_value + count 
                value = value // 10
            value = count
        return value  
        
result = Solution().addDigits(38)
print(result)
