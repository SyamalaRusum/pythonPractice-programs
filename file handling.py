#create a file and read the file line by line and aalso read multiple lines into a list

file=open("txtfile.txt","r")
print(file.readline())      #it reads the file and print the single line
print(file.readline(22))    #it prints the text up to the limit we mentioned
print(file.readlines())     #it prints the entire file in a list format
print(file.readlines(10))



#reading data from the data.txt file
def func():
    with open ("data.txt","r") as file:
        print(file.read())
func()

#write the data to the file
def func():
    with open ("data.txt","w") as file:
        file.write("hello python")
func()

#append data to the existing file
def func():
    with open ("data.txt","a") as file:
        file.write("welcome")
func()

#read audio file
def func():
    with open ("audio.mp3","r") as file:
        print(file.read())
func()