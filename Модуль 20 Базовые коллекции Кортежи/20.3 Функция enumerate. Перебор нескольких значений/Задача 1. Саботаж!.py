string = input('Строка: ')

print('Ответ:', end=' ')
for index, value in enumerate(string):
    if value == '~':
        print(index, end='')
