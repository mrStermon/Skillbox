try:
    user_str = int(input('Введите сюда что-нибудь: '))
    with open('result.txt', 'w') as result_file:
        result_file.write(str(user_str))
except FileExistsError as error:
    print(error)
except TypeError as error:
    print(error)
else:
    print('Никаких ошибок не было замечено.')
finally:
    with open('result.txt', 'w', encoding='utf-8') as result_file:
        result_file.write('Нашли ли вы ошибку или нет, мне всё равно')
