def histogram(string):
    letters_dict = {}
    for i_letter in string:
        if i_letter in letters_dict:
            letters_dict[i_letter] += 1
        else:
            letters_dict[i_letter] = 1

    return letters_dict


text = input('Введите текст: ')
hist = histogram(text)

for i_sum in sorted(hist.keys()):
    print(i_sum, ':', hist[i_sum])

print('Максимальная частота:', max(hist.values()))
