import os


path = input('Путь: ')

if os.path.exists(path):
    if os.path.isfile(path):
        print('Это файл', '\nРазмер файла:', os.path.getsize(path), 'байт')
    elif os.path.isdir(path):
        print('Это путь', path)
else:
    print('Указанного пути не существует')
