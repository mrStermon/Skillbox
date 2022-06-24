phonebook = dict()

while True:
    string = input('Введите имя, фамилию и номер: ').split()
    if string == ['end']:
        break
    elif (string[0], string[1]) in phonebook:
        print('\nДанный контакт уже есть в телефонной книге')
    else:
        phonebook[(string[0], string[1])] = int(string[2])

    for i_person in phonebook:
        print('{0} {1} — {2}'.format(i_person[0], i_person[1], phonebook[i_person]))
