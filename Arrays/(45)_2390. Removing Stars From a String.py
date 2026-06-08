
# 2390. Removing Stars From a String
s = "leet**cod*e"
Output= "lecoe"
new_s = []  # stack
for char in s:
    if char == "*":
        new_s.pop()
    else:
        new_s.append(char)

print("".join(new_s))

'''
o(n),o(n)
append in stack with removing the before element using pop w 
'''