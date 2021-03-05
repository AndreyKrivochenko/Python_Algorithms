"""
    В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
    являться минимальными), так и различаться.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_elem = 101
min_elem_next = 101

for _, item in enumerate(array):
    if item < min_elem_next:
        min_elem_next = item
    if min_elem_next < min_elem:
        min_elem_next, min_elem = min_elem, min_elem_next
print(f'1: {min_elem}\n2: {min_elem_next}')
