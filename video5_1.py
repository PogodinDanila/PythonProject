#функция пример
def print_numbers(limit):
    for i in range(limit):
        print(i)

n = int(input())
print_numbers(n)

#функция с пустым аргументом
def hello():
    print("Hello world")
    print("this text gets printed from a function")

hello()
hello()