        
s = "abc" 
t = "ahbgdc"
i = 0 
j = 0 
while i < len(s) and j < len(t): 
    if  t[j] == s[i]:
        i += 1 
    j += 1
    
print(i == len(s))