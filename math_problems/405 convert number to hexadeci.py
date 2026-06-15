class Solution:
    def toHex(self, num: int) -> str:
        if num == 0 : 
            return "0"
        
        hexa_lett = "0123456789abcdef"
        
        if num < 0:
            num = num + (1<<32)
        result = ""
        while num > 0 : 
            result = hexa_lett[num % 16] + result
            num //= 16

        return result 

num = 26
solution = Solution()
result = solution.toHex(num)
print(result)

'''
    if num is 0 return "0"
    if num is negative convert it to positive by adding 2^32
    then we can find the hexadecimal representation by repeatedly dividing the number by 16 and taking the remainder
    we can use a string of hexadecimal characters to map the remainders to their corresponding hexadecimal digits
    we keep adding the hexadecimal digits to the result string until num becomes 0
    time complexity O(log n) where n is the input number and space complexity O(1)
'''