arr = [1,2,3,4,5,6,7,8,9,10]

start = 0
k = 3
output = []

while start < len(arr):
    end = min(k, len(arr))
    
    total = 0   # reset for each block
    for i in range(start, end):
        total += arr[i]   # accumulate
    
    output.append(total)
    
    start = end
    k *= 2

print(output)