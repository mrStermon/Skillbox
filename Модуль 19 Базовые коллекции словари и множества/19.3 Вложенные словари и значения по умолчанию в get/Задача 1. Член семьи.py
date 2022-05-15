family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

child_surname = ''

for child in family_member.get('children'):
    if child.get('name') == 'Bob':
        child_surname = child.get('surname', 'nosurname')

print(child_surname)

# альтернативное решение вопроса
# if any(child.get('name') == 'Bob' for child in family_member.get('children', [])):
#     print('Есть')
# else:
#     print('Нету')




