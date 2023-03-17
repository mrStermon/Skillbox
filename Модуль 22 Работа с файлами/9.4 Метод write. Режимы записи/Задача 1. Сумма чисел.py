file = open('numbers.txt', 'r')
result = 0
for i in file:
    result += int((i.replace('\n', '')))

result_file = open('answer.txt', 'w')
result_file.write(str(result))
file.close()
result_file.close()
