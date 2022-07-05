#вложенность циклов
x = int(input("x = "))

if 0<x<7:
    print ("Value is in range, let's continue")
    y = 2 * x - 5
    if y<0:
        print("y is negative")
    else:
        if y>0:
            print("y is possitive")
        else:
            print ("y=0")
#более оптимальный вариант
x = int(input("x = "))

if 0<x<7:
    print ("Value is in range, let's continue")
    y = 2 * x - 5
    if y<0:
        print("y is negative")
    elif y>0:
        print("y is possitive")
    else:
        print ("y=0")