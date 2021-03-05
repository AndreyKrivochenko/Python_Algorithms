"""
    Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count_array = [[], []]
for _, item in enumerate(array):
    if item in count_array[0]:
        count_array[1][count_array[0].index(item)] += 1
    else:
        count_array[0].append(item)
        count_array[1].append(1)

max_count = 0
max_index = 0
for i, item in enumerate(count_array[1]):
    if item > max_count:
        max_count = item
        max_index = i
print(f'Чаще всего встречается число - {count_array[0][max_index]}, встретилось {max_count} раз(-а)')

