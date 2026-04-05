# Input: s = "abcabcbb"
# Output: 3

# brute force o(n2)
s = "abcabcbb"
max_len = 0 

for i in range(len(s)):
    _seen = set()
    for j in range(i, len(s)):
        if s[j] in _seen:
            break
        _seen.add(s[j])
        max_len = max(max_len, j-i +1)
    
print(max_len)

# obtimized soultion o(n)
left = 0 
seen = set()
max_length = 0 
for right, char in enumerate(s):
    while char in seen:
        seen.remove(s[left])
        left +=1 
    seen.add(char)
    max_length = max(max_length,right-left+1)
print(max_length)