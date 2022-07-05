#Строки

string1 = 'String\'s'
string2 = "string"

print(string1, string2)

string = "First line of text.\n"\
    "second line of text."
print(string)

multiline_string = """Lesson2. Variables and data type.
 Some data types:
 -int
 -float
 -bool
 -complex
 -str
 """
print(multiline_string)

# ввод строки и числа
string = input('Enter a tring: ')
print('You have entered "{}"'.format(string))

print ('Press Enter to continue...')
input()

n = int(input('First number: '))
m = int(input('second number: '))
print('{} + {} = {}'.format(n, m, n+m))