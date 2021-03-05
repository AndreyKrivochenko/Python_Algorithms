"""
    В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
    минимальный и максимальный элементы в сумму не включать.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_elem = array[0]
max_elem = array[len(array) - 1]
for _, item in enumerate(array):
    if item < min_elem:
        min_elem = item
    elif item > max_elem:
        max_elem = item

if array.index(min_elem) < array.index(max_elem):
    start_index = array.index(min_elem) + 1
    end_index = array.index(max_elem)
else:
    start_index = array.index(max_elem) + 1
    end_index = array.index(min_elem)

sum_elem = 0
for i in range(start_index, end_index):
    sum_elem += array[i]

print(f'Сумма элементов между {array[start_index - 1]} и {array[end_index]} равна {sum_elem}')
