"""
    Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.Количество вводимых
    чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

    Проверял на Windows 10 x64, Python 3.9.2
    Вводимых чисел: 3
    Цифра для поиска: 6
    число 1 - 87662437664
    число 2 - 9080865214564
    число 3 - 9864215765284653
"""

import sys
from collections import Counter


def calc(obj):
    if not hasattr(obj, '__iter__') or isinstance(obj, str):
        return sys.getsizeof(obj)
    else:
        res = 0
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                res += calc(key)
                res += calc(value)
        elif not isinstance(obj, str):
            for item in obj:
                res += calc(item)
        return res


# Вариант 1
# В моём случае - Под переменные в памяти было выделено 172 байт
def find_1():
    count = int(input('Введите количество вводимых чисел: '))
    dig = int(input('Введите цифру для поиска: '))
    summ = 0
    summ_byte = 0
    for i in range(1, count + 1):
        number = int(input(f'Введите {i} число: '))
        if summ_byte < calc(number):
            summ_byte = calc(number)
        while number != 0:
            if number % 10 == dig:
                summ += 1
            number //= 10
        if i == count:
            summ_byte += calc(i)
    print(f'Цифра {dig} встретилась {summ} раза')
    summ_byte = summ_byte + calc(count) + calc(dig) + calc(summ) + calc(summ_byte)
    print(f'Под переменные в памяти было выделено {summ_byte} байт')


# Вариант 2
# В моём случае - Под переменные в памяти было выделено 957 байт
def find_2():
    count = int(input('Введите количество вводимых чисел: '))
    dig = int(input('Введите цифру для поиска: '))
    summ_byte = 0
    summ = Counter()
    for i in range(1, count + 1):
        number = input(f'Введите {i} число: ')
        if summ_byte < calc(number):
            summ_byte = calc(number)
        for num in number:
            summ[num] += 1
        if i == count:
            summ_byte += calc(i)
    print(f'Цифра {dig} встретилась {summ[str(dig)]} раз(а)')
    summ_byte = summ_byte + calc(count) + calc(dig) + calc(summ_byte) + calc(summ)
    print(f'Под переменные в памяти было выделено {summ_byte} байт')


# Вариант 3
# В моём случае - Под переменные в памяти было выделено 223 байт
def find_3():
    count = int(input('Введите количество вводимых чисел: '))
    dig = input('Введите цифру для поиска: ')
    summ = ''
    summ_byte = 0
    for i in range(1, count + 1):
        summ += input(f'Введите {i} число: ')
        if i == count:
            summ_byte += calc(i)
    print(f'Цифра {dig} встретилась {summ.count(dig)} раз(а)')
    summ_byte = summ_byte + calc(count) + calc(dig) + calc(summ_byte) + calc(summ)
    print(f'Под переменные в памяти было выделено {summ_byte} байт')


# find_1()
# find_2()
find_3()

""" Первый вариант лучший в плане потребления памяти, так как в нем используются только целочисленные переменные.
    Массивы и строки занимают больше памяти"""