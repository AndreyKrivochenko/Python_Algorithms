"""
    Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
    представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
    их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
    произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

    Сделал только сложение, умножение не успеваю... Буду думать как уменьшить программу, уж больно монструозно вышло
"""
from collections import deque

SUMM_MATR = [
    ['0', '1', '2',	'3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10'],
    ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11'],
    ['3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12'],
    ['4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13'],
    ['5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14'],
    ['6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14', '15'],
    ['7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16'],
    ['8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16', '17'],
    ['9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
    ['A', 'B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
    ['B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A'],
    ['C', 'D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B'],
    ['D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C'],
    ['E', 'F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C', '1D'],
    ['F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C', '1D', '1E']
]

HEX_DICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def summation_one(a: str, b: str):
    return SUMM_MATR[HEX_DICT[b]][HEX_DICT[a]]


def summation(a: str, b: str):
    a = a.upper()
    b = b.upper()
    summa = deque()
    first = list(i for i in a)
    second = list(i for i in b)
    if len(first) < len(second):
        first, second = second, first
    one = False
    for _ in range(len(first)):
        if len(second) > 0:
            spam = list(i for i in summation_one(first.pop(), second.pop()))
            if one:
                if len(spam) > 1:
                    summa.appendleft(summation_one(spam[1], '1'))
                    one = True
                else:
                    summa.appendleft(summation_one(spam[0], '1'))
                    one = False
            else:
                if len(spam) > 1:
                    summa.appendleft(spam[1])
                    one = True
                else:
                    summa.appendleft(spam[0])
        else:
            if one:
                spam = list(i for i in summation_one(first.pop(), '1'))
                if len(spam) > 1:
                    summa.appendleft(spam[1])
                    one = True
                else:
                    summa.appendleft(spam[0])
                    one = False
            else:
                summa.extendleft(first[::-1])
                break
        if len(first) == 0 and one:
            summa.appendleft('1')

    return ''.join(i for i in summa)


print(summation('a2DDffa98', 'c4fdefaf36'))
