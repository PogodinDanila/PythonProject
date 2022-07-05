#срезы
my_list = [5, 7, 9, 1, 1, 2]
sub_list = my_list[:3]
print(sub_list)

print(my_list[2:-2])
print(my_list[4:5])


sub_list = my_list[:-1:2]
print(sub_list)

print(my_list[2:-2:2])
print(my_list[::-1])
#операции со списками
my_list = [5, 7, 9, 1, 1, 2]

value = int(input("Enter a number: "))
if value in my_list:
    print("This number is in list")
else:
    print("This number is not in list")

print("Number of elements:", len(my_list))