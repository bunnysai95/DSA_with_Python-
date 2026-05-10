def trailingZeroes(n: int) -> int:
    # i = 1 
    result = 1
    while n > 0: 
        result = result* n
        n -= 1
    count =0 
    while result > 0 and result % 10 ==0 :
        count += 1
        result = result//10 
    return count 
print(trailingZeroes(5),"zero's")