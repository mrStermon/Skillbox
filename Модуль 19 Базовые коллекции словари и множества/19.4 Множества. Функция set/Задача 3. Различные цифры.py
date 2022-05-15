string = 'ab1n32kz2'

nums = {i for i in string if '0' <= i <= '9'}
print('Различные цифры строки:', ''.join(nums))
