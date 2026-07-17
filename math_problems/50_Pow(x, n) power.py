class Solution:
    def myPow(self, x: float, n: int) -> float:
        # effectivate way
        def helper(x, n):
            if x == 0 : return 0 
            if n == 0 : return 1 

            res = helper(x, n//2)
            res = res * res
            return x * res if n % 2 else res 
        res = helper(x , abs(n))

        return res if n >= 0 else 1 / res 


result = Solution().myPow(2.00000, 10)
print(result)
        
        # if n == 0 : 
        #     return 1 
        # if n <= 0: 
        #     i = 1
        #     temp_value = x
        #     n_neg = -n 
        #     while i < n_neg : 
        #         temp_value = temp_value * x   
        #         i += 1
        #     return 1 / temp_value 
        # else:
        #     i = 1
        #     temp_value = x
        #     while i < n : 
        #         temp_value = temp_value * x
        #         i += 1 
        #     return  temp_value 


