Input= [2, 2, 3, 4, 4]
Output= 3


count = {}

for num in Input:
    count[num] = count.get(num,0)+1
    '''count.get(n, 0) means:
"Look for n in dictionary"
"If FOUND    → return its value"
"If NOT FOUND → return 0 (default)"'''

# finding which has count 1 
for key, val in count.items():
    if val == 1:
        print(key) 


'''
time complexy(o(n), space(n))
solving , every number repetation storing in dic,
with loop getting the count of key, val from dict == 1 returning the key for val
'''
# optimized soultion 
# o(n), space o(1)

result = 0 
for val in Input:
    result ^= val

print(result)

'''
^= n  means:
"XOR my result with n"
"If n appeared before → cancel it to 0"
"If n is new → keep it"
"Last man standing = single number!" '''