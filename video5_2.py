def print_number(limit):
    for i in range(limit):
        print(i)

print_number(3)
print()
print_number(5)

print()

#функция в функцие
def print_number(limit):
    for i in range(limit):
        print(i)

def main():
    print_number(3)
    print()
    print_number(5)
main()
