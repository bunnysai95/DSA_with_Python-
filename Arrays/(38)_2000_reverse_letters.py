# 2000. Reverse Prefix of Word
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = list(word)
        i = 0
        while i < len(s):
            if s[i] == ch:
                l , r = 0, i
                while l < r :
                    s[l],s[r] = s[r],s[l]
                    l+=1
                    r-=1
                break
            i+=1
        return ''.join(s) 
solution = Solution()
word = "abcdefd"   
ch = "d"
result = solution.reversePrefix(word, ch)
print(result)