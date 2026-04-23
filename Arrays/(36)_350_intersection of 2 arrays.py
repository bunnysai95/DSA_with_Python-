nums1 = [1,2,2,1]
nums2 = [2,2]

nums1.sort()
nums2.sort()

i , j = 0 , 0 
new_list = []
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        new_list.append(nums1[i])
        i += 1
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1 
    else:
        j +=1 

print(new_list)

