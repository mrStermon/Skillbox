import math


def cylinder(r, h):
    s = math.pi * r ** 2
    side = 2 * math.pi * r * h
    full = side * 2 + s
    return side, full


radius = float(input('Введите радиус: '))
height = float(input('Введите высоту: '))
result = cylinder(radius, height)
print('\nПлощадь боковой поверхности: {0:.2f} \nПолная площадь: {1:.2f}'.format(result[0], result[1]))
