class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1
        def is_palidrom(i,j):
            while i < j :
                if s[i]!=s[j]:
                    return False
                i += 1 
                j -= 1
            return True
        while i < j : 
            if s[i]==s[j]:
                i += 1 
                j -= 1
            else: 
                return is_palidrom(i+1,j) or is_palidrom(i, j-1)
        return True 

        

solution = Solution()
s = "abca"
result = solution.validPalindrome(s)
print(result)