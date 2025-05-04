#def add(x, y):
#    return x + y
# вызываем функцию
#add(1, 2)
#print(add(1, 2))
#print(add('I am ', 'tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

print(arg(1, 1, 1))

print(arg(2, 2, '1', 1))
#должна быть ошибка, т.к. нельзя складывать целые числа и строки, разные типы


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '1', '1', '1'))

print(range_arg('1', '1', d='3', c='4'))
