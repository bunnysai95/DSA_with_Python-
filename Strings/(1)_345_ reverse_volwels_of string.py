# 345. Reverse Vowels of a String
s = "IceCreAm"
v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
r = list(s)
left , right = 0, len(s)-1
while left < right: 
    if r[left] not in v:
        left +=1 
    elif r[right] not in v:
        right -=1 
    else:
        r[left], r[right] = r[right], r[left]
        left +=1 
        right -=1
print("".join(r))

# optimized solution 
vowels = "aeiouAEIOU"
s = list(s)
for i in s:
    if i in vowels:
        s.remove(i)
        s.insert(0, i)
print("".join(s))