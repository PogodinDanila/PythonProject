x = float(input('first number: '))
y = float(input('second number: '))
operation = input('operation: ')

result = None

if operation == '+':
    result = x+y
elif operation == '-':
    result = x-y
elif operation == '*':
    result = x*y
elif operation == '/':
    result = x/y
else:
    print('unsupported operation')

if result is not None:
    print ('Result:', result)