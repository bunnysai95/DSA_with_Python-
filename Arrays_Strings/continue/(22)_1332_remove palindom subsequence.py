s = "ababa"
output = 1
'''here question remove subsequence
1. if the string is empty return 0
2. if the string is palindrome return 1 
3. if the string is not palindrome return 2 
because we can remove all a's and then all b's or vice versa'''

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s : return 0 
        l, r = 0 , len(s)-1
        while l < r: 
            if s[l] != s[r] : return 2
            l +=1 
            r-=1
        return 1 

solution = Solution() 
result = solution.removePalindromeSub(s)
print(result)
