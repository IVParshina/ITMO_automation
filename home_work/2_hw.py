
def optional(a: int, b: float, c: str, d: list, h: bool) -> list:
#    print(f'{a}')
#    print(f'{b}')
#    print(f'{c}')
#    print(f'{d}')
#    print(f'{h}')
    return [type(a), type(b), type(c), type(d), type(h)]
print(optional(8, 4.2, 'Ура', [3,4,5], True))




a: int = 5
b: float = 3.5
def square(rad: float) -> int:
    return round(rad ** 2)

print(square(14.2))


def new_list(by_list: list) -> list:
    r = by_list[0:3]
    return r

print('Срез списка c первого по третий элемент: ', new_list([1, 2, 3, 5, 8, 13, 21]))






