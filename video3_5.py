#работа с элементами в списке
from typing import List, Any

my_list = []

my_list.append(3)
my_list.append(5)
my_list.append(my_list[0]+my_list[1])

print(my_list)

del my_list[2]
print(my_list)

#числа фибаначе
n = 10

fibs = [1, 1]

for i in range(n-2):
    fibs.append(fibs[i]+fibs[i+1])
print(fibs)