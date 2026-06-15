num = 16 
x = num
while x*x > num:
    x = (x+num // x) // 2
print(x*x == num)


# this is newton's method to find the square root of a number