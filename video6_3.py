#вложенные функции
def outer_function():
    def inner_function():
        print("INner function")
    print("Outer function")
    inner_function()

outer_function()

#существование переменной
print("example 1")
def function():
    print(var)

var = "global variable"
function()

print("example 2")
def function():
    bar = "local variable"
    print(var)

bar = "global variable"
function()
print(bar)
