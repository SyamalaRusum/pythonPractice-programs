def func():

    try:
        file = open("txtfile1.txt.txt", "r")
        print(file.read())
        file=open("txtfile1.txt","w")
        x=file.write("We are here to help you with every step on your journey and come up with a curriculum that is designed for students and professionals who want to be a Python developer.")
        print(x)
    except FileNotFoundError as e:
        print("exception:File not found successfully handled")

func()