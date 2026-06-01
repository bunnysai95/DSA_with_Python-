from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0 
        temp = 0 
        while i < len(arr):
            if arr[i] == 0 :
                for j in range(len(arr) - 1, i, -1):   # shifting right to left # output = [1,0,0,2,3,0,4,5]
                    arr[j] = arr[j - 1]
                i +=2
            else:
                i +=1 

arr = [1,0,2,3,0,4,5,0]
solution = Solution()
solution.duplicateZeros(arr)
print(arr)



        