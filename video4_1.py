#условия пример 1
number = int(input("Enter a number: "))
if number > 5:
    print("THis number isgreater then five")

x = float(input("x = "))

if x>0:
    y = x ** 0.5
else:
    y = x ** 2
print(y)
#пример 2
name = input("Enter your name: ")

if name == "Alexey":
    print("You have entered", name)
    print("this is vy name, too.")
else:
    print("Your name differs from mine.")