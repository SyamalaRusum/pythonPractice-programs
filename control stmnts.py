#fibonacci using for loop

num1, num2 = 0, 1
print("Fibonacci sequence:")
for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res

#factorial using for loop
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

#while loop
#print the reverse of a num

n = int(input("Enter number: "))
rev = 0
while(n != 0):
   rem = n % 10
   rev = rev * 10 + rem
   n = n // 10

print(rev)