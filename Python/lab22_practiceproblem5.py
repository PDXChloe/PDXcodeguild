# Problem 5
#
# Write a function that merges two lists into a single list, where each element of
# the outlist list is another list containing two elements.
#
# merge([5,2,1], [6,8,2]) -> [[5,6],[2,8],[1,2]]
#
l_one = [5,2,1]
l_two = [6,8,2]
l_merge = []

for i in range(len(l_one)):

    l_merge.append([l_one[i], l_two[i]])
print(l_merge)



