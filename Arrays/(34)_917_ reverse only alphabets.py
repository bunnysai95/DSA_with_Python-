'''
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Input: s = "ab-cd"
Output: "dc-ba"
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
'''


from typing import List
s = "ab-cd"
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char = list(s)
        i = 0 
        j = len(s)-1 
        while i < j :
            if not s[i].isalpha():
                i +=1 
            elif not s[j].isalpha():
                j -= 1 
            else:
                char[i], char[j] = char[j], char[i]
                i +=1
                j -=1
        return ''.join(char)
    

solution = Solution()
result = solution.reverseOnlyLetters(s)
print(result)

    