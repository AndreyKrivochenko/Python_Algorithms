"""
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_index = 0
max_index = SIZE - 1
min_elem = array[min_index]
max_elem = array[max_index]
for i, item in enumerate(array):
    if item < min_elem:
        min_elem = item
        min_index = i
    elif item > max_elem:
        max_elem = item
        max_index = i
array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)
