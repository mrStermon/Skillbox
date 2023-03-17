import os


path_example = os.listdir(os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic')))
print('Содержимое каталога:', os.path.abspath(os.path.join('..', '..', 'Python_Basic')))

for i_elem in path_example:
    print('\t', os.path.abspath(os.path.join('..', '..', 'Python_Basic', i_elem)))
