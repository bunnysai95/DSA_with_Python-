
n = 5
for i in range(n):
    for j in range(n -i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

n = 4
for i in range(n):
    for j in range(n):
        if i ==0 or i == n-1 or j ==0 or j == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

def hollow_square(side):
    for i in range(side): # Outer loop for rows
        for j in range(side): # Inner loop for columns
            # Check if the current position is on the border
            if i == 0 or i == side - 1 or j == 0 or j == side - 1:
                print("*", end="") # Print asterisk for edges
            else:
                print(" ", end="") # Print space for the interior
        print() # Move to the next line after each row

# Example: Create a hollow square with a side length of 5
hollow_square(5)
