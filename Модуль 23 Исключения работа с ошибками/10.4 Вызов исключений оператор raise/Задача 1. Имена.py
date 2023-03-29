file_name = open('people.txt', 'r')
summ_sym = 0
word = ''

try:
    for i in file_name:
        word += i.replace('\n', '')
        if len(word) < 3:
            raise BaseException
        else:
            summ_sym += len(word)
            word = ''
except BaseException:
    print('Нашлась ошибка')
    print(summ_sym)