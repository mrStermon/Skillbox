import random


rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

list_1 = [rus_alphabet[random.randint(0, 32)] for i in range(10)]
list_2 = [rus_alphabet[random.randint(0, 32)] for j in range(10)]

print('Первый список:', list_1)
print('Второй список:', list_2)

dict_1 = {key: value for key, value in enumerate(list_1)}
dict_2 = {key: value for key, value in enumerate(list_2)}

print('\nПервый словарь:', dict_1)
print('Второй словарь:', dict_2)
