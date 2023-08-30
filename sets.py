#add items into sets

sample_set = {"Yellow", "Orange", "Black"}
sample_list = {"Blue", "Green", "Red","Orange","Black"}

sample_set.update(sample_list)
print(sample_set)

#
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

#unique elements
print(set1.union(set2))

#program to update the first set with items that exist only in the first set and not in the second set.
set1.difference_update(set2)
print(set1)

#Remove items from set1 that are not common to both set1 and set2
set11 = {10, 20, 30, 40, 50}
set22 = {30, 40, 50, 60, 70}
set11.intersection_update(set22)
print(set11)

#Update set1 by adding items from set2, except common items
set1.symmetric_difference_update(set2)
print(set1)