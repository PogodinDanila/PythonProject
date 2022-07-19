#while_example1

responce = ""
while responce != "exit":
    responce = input("Type 'exit' to exit: ")

#while_example2
n = 1
while n <=3:
    print('n = ', n)
    n += 1

#while_example3
number = 0
while number <= 0:
    number = int(input('Enter a positive integer: '))
    print("You have entered", number)