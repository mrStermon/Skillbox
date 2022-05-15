import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
nums_1 = set(nums_1)
nums_2 = set(nums_2)
min_nums_1 = min(nums_1)
min_nums_2 = min(nums_2)
random_number_1 = random.randint(100, 200)
random_number_2 = random.randint(100, 200)

print('1-е множество:', nums_1)
print('2-е множество:', nums_2)

print('\nМинимальный элемент 1-го множества:', min_nums_1)
print('Минимальный элемент 2-го множества:', min_nums_2)
nums_1.discard(min_nums_1)
nums_2.discard(min_nums_2)

print('\nСлучайное число для 1-го множества:', random_number_1)
print('Случайное число для 2-го множества:', random_number_2)
nums_1.add(random_number_1)
nums_2.add(random_number_2)

united_nums = nums_1 | nums_2
intersection_nums = nums_1 & nums_2
print('\nОбъединение множеств:', united_nums)
print('Пересечение множеств:', intersection_nums)
print('Элементы, входящие в nums_2, но не входящие в nums_1:', nums_2 - nums_1)
