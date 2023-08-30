#checking dublicate items in tuple or not
def has_duplicates(tuple_data):
    # Convert the tuple to a list for easy manipulation
    data_list = list(tuple_data)

    # Check if the length of the list is equal to the length of the set
    # If they are equal, it means there are no duplicates
    if len(data_list) == len(set(data_list)):   #set creates a set obj The items in a set list are unordered, so it will appear in random order.
        return False
    else:
        return True

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 3, 4, 5)

print(has_duplicates(tuple1))  # False
print(has_duplicates(tuple2))

#reverse a tuple
t=tuple1[::-1]
print(t)

#unpack the tuple into var's
a, b, c, d, e = tuple1
print(a)
print(b)
print(c)
print(d)
print(e)

#swap
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

#count number of 5's
print(tuple1.count(5))