#if

list_of_numbers = [2,4,6,9,5]
for i in list_of_numbers:
        if i % 2 != 0:
                print(i, "is an odd number")
        if i % 2 == 0:
                print(i, "is an even number")

#program to print even num,if num is divisible by 6 then continue
for i in range(1,50):
    if i%2==0:
        print(i)
    if i%6 == 0:
        continue


#if-else
#python program to check if a number is odd and divisible by 3

list_of_numbers = [4, 5, 9, 17, 21]
for i in list_of_numbers:
    if i % 2 != 0:

        if i % 3 == 0:
            print(i, "is an odd number & divisible by 3")

        else:
            print(i, "is an odd number but not divisible by 3")
    else:
        print(i, "is an even number")



#if elif else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)