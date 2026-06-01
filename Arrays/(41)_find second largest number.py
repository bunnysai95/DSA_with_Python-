array = [2, 3 , 5, 8, 10, 2, 5, 15]
# finding max number in the array 
second_largest = sorted(set(array))[-2]
print(second_largest)


largest = -1
second_largest = -1

for num in array:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)

