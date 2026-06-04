'''
Long Pressed Name
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0 
        j = 0 
        while j < len(typed) and i < len(name):
            if  name[i] == typed[j] :
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:  
                return False
            j += 1 
        return i == len(name)  
name = "alex"
typed = "aaleex"    
solution = Solution()
result = solution.isLongPressedName(name, typed)
print(result)