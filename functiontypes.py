# types of functions

#Keyword arguments
def func1(name,age):
    print("name: ",name)
    print("age ",age)
func1(age=10,name="hi")

#default arguments
def func(a=10,b=20):
    if(a>b):
        print('a is big')
    else:
        print('b is big')
func()


#positional arguments
def func2(name,age):
    print("name: ",name, "age" ,age)
func2(23,"hi")


#variable number of arguments
def func3(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s"%(key,value))
func3(first='hi',mid='hello',lst='welcome')