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


# =============3rd largest =======================

array = [2, 3 , 5, 8, 10, 2, 5, 15]
largest = -1
second_largest = -1
third = -1


for num in array:
    if num > largest:
        third = second_largest
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        third = second_largest
        second_largest = num
    elif num > third and num != largest and num != second_largest:
        third = num

print(third)
print(second_largest)


'''
swaping the number and cheking whether same or not '''