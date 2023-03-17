import os

# user_path = input('Ищем в: ')
# user_file = input('Имя файла: ')
# find_file(user_path, user_file)


def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            print('\t', os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


user_path = input('Ищем в: ')
user_file = input('Имя файла: ')
print('Найдены следующие пути: ')
find_file(user_path, user_file)
