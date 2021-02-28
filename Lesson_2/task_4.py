"""
    Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится
    с клавиатуры.
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=Io6JtZSmKl5rpe6xkkA8&title=Lesson_2#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D16XIekX5LPrGtcChYSI4K3b0VL_E25oFC%26export%3Ddownload
"""


def func(number, count, col):
    if count == col:
        return number
    else:
        return number + func(number / 2, count + 1, col)


n = int(input('Введите количество элементов: '))
num, i = 1, 1
result = func(num, i, n)

print(f'Сумма {n} элементов равна {result}')
