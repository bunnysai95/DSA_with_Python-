
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0 
        for i in range(n+1):
            num = i 
            while num>0:
                if i % 10 == 1  :
                    count +=1   
                    i //= 10 
        return count 
""" 
i m reading number 
if it is mulitiple digts in number them i dividing with 10 and checking last number 1/not counting it """
# optimized solution 

def countDigitOne_1(self, n: int) -> int:
    if n < 0:
        return 0
    count = 0  # counting 1's
    digit = 1 # 1 loop, 10 loop's, 100 loop's, 1000 loop's
    while digit <= n:
        high = n // (digit *10) # divides number 213 has 2.13 = 2,200 -loop's
        currrent = (n//digit) % 10  
        low = n % digit
        if currrent == 0 : 
            count += high* digit
        elif currrent == 1 :
            count += high * digit + low +1
        else:
            count += (high + 1) * digit
        digit *= 10 
        
    return 1



result = Solution().countDigitOne(13)
print(result)
