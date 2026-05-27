class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0 :
            return False
        for value in [2,3,5]:
            while n % value == 0 :
                n //= value  
        return n == 1  
        # or
        # if n <= 0:
        #     return False
        # while n % 2== 0 :
        #     n //= 2
        # while n %3 == 0: 
        #     n //=3 
        # while n %5 ==0:
        #     n//=5
        # return n == 1 

result = Solution().isUgly(6)
print(result)

"""
i m caliculating value whether 2, 3 5 is could be divisible to the given number
if it vinds to ==0 ten it is / if not it is not Return False  
"""