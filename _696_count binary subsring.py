class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0 
        current_length = 1
        previous = 0 
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                current_length +=1 
            else:
                result += min(previous, current_length)
                previous = current_length 
                current_length = 1
        result += min(previous, current_length )
        return result 
    
s = "00110011"
solution = Solution()   
result = solution.countBinarySubstrings(s)
print(result)