#список-строка
string = "a string"

print(string[0])
print(string[-1])

print(string[2:5])
print(string[::2])
print(string[::-1])

print(string[2] + string[-3:])

string = input("Enter a string: ")
if "q" in string:
    print("There a 'q' in the string")
else:
    print("There isn't a 'q' in the string")

print("ing" in "sing")

string = input("Enter a string: ")
print(len(string))

