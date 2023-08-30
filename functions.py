#calculator using functions
def add(num1, num2):
   return num1 + num2

def sub(num1, num2):
   return num1 - num2

def mul(num1, num2):
   return num1 * num2

def div(num1, num2):
   return num1 / num2

op=input("enter a operation: ")
num1=int(input("enetr a number1: "))
num2=int(input("enter a number2: "))
if op == 'add':
    print("addition is:",add(num1,num2))
elif op == 'subtract':
    print("subtraction is: ",sub(num1,num2))
elif op == 'multiply':
    print("multiply: " ,mul(num1,num2))
elif op == 'divide':
    print("division: ",div(num1,num2))
else:
    print("invalid operation")


#accessing data structures using functions
def func_():
    li=[2,5,3,1,77,"hii",8,34,99,5]
    tup=(4,6,7,22,44,13,5,"hello")
    dic={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    print(li, type(li))
    print(tup, type(tup))
    print(dic, type(dic))
func_()


