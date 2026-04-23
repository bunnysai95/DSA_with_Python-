# A phrase is a palindrome if, 
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# noon, peep, poop, toot

# obtimized solution
Palindrome = "A man, a plan, a canal: Panama"
import re
def is_palindrome(s):
    pattern = r'[^a-zA-Z0-9]'
    cleaned_s = re.sub(pattern, '', s).lower()
    return cleaned_s == cleaned_s[::-1]
result = is_palindrome(Palindrome)
print(result)

s = "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowered = s.lower()
        i , j = 0 , len(s_lowered) - 1
        while i < j :
            while i < j and not s_lowered[i].isalnum():
                i +=1
            while i < j and not s_lowered[j].isalnum():
                j -=1
            if s_lowered[i] == s_lowered[j]:
                i +=1
                j -=1
            else: 
                return False 
        return True 
solution = Solution()
result = solution.isPalindrome(s)
print(result)