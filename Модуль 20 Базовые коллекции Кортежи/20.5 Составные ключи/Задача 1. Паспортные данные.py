def issue():
    serial = int(input('Введите серию: '))
    number = int(input('Введите номер: '))

    for i_person in data:
        if serial and number in i_person:
            print(data[i_person][1], data[i_person][0])


data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
    }

issue()
