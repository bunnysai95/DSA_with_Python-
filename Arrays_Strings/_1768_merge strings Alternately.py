def mergeAlternately(self, word1: str, word2: str) -> str:
        new_list = []
        i = 0 
        j = 0 
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                new_list.append(word1[i])
                i += 1
            if j < len(word2):
                new_list.append(word2[j])
                j += 1
        return ''.join(new_list)
word1 = "abc"
word2 = "pqr"       
result = mergeAlternately(1,word1, word2)
print(result)