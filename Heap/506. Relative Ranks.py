score = [5,4,3,2,1]
output = ["Gold Medal", "Silver Medal", "Bronze Medal",4,5]
score_1 = [10,3,8,9,4]
output_1 = ["Gold Medal", 5, "Silver Medal", "Bronze Medal", 4]

sorted_list = sorted(score_1, reverse= True)
count = {}

for i in range(len(sorted_list)):
    if i == 0:
        count[sorted_list[i]] = "Gold Medal"
    elif i == 1:
        count[sorted_list[i]] = "Silver Medal"
    elif i == 2:
        count[sorted_list[i]] = "Bronze Medal"
    else:
        count[sorted_list[i]] =str(i +1)

result = []
for i in score_1:
    result.append(count[i])
print(result)

"""
sorted list using revere
then i have assigned there positions
then i have loopd back to the orginal postion 
"""


