#рекурсия
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)
print(recursive_factorial(10))

#числа фибаначе
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1, 11):
    print(fib(i))