string = 'Я! Есть. Грут?! Я, Грут и Есть.'
symbols = set(".,;:!?")
count = 0
for i_sym in string:
    if i_sym in symbols:
        count += 1

print('Количество знаков пунктуации:', count)
