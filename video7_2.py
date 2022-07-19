#break_example

while True:
    print('Enter "exit" to exit loop')
    response = input(">")
    if response == "exit":
        break
    print("loop has stopped")


#break_example2
while True:
    print("Menu: ")
    print("1. Enter your name")
    print("2. Print greeting")
    print("3. Quit")
    response = input("Please choose an action: ")
    print()
    if response =="1":
        name = input("Enter your name:")
    elif response =="2":
        if name:
            print("Hello, ", name, "!", sep = "")
        else:
            print("I don`t know your name.")
    elif response == "3":
        break
    else:
        print("Incorrected input")
        print()
