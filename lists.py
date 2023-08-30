#lists
#accessing the lists
languages = ["Python", "Swift", "C++"]

print(languages[0])
print(languages[2])

#slicing

my_list = ['p','r','o','g','r','a','m','i','z']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

#operations

li=[21, 34, 54, 12, 32]
li.append(45)
print(li)

li[2]=0     #changing value at 2nd position
print(li)

del li[2]
print(li)
del li[2:5]
print(li)

li.append(35)
print(li)

del li      #deletes the entire file

for i in my_list:
    print(i,type(i))

#Find and print the sum of all even numbers in the list.
li = [2, 1, 55, 76, 84, 2, 45, 9]
li1 = []
for i in li:
    if i % 2 == 0:
        li1.append(i)
print("before printing the even num list is: ", li)
print("even num in the list : ", li1)
print("the sum of even num in the list: ", sum(li1))

# print max value in the list
li = [2, 1, 55, 76, 84, 2, 45, 9]
print(max(li))

# using sort method to print the max element
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])

# using for loop to print the max value in list

lst = [20, 49, 1, 99]
largest = lst[0]

for i in lst:
    if i >= largest:
        largest = i

print(largest)

# print list values >10
li = [2, 1, 55, 76, 84, 2, 45, 9]
li2 = []
for i in li:
    if i >= 10:
        li2.append(i)
print(li2)

