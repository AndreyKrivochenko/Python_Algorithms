"""
    В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
    к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative = MIN_ITEM
max_negative_index = 0
for i, item in enumerate(array):
    if 0 > item > max_negative:
        max_negative = item
        max_negative_index = i

print(f'Максимальный отрицательный элемент: {max_negative}, позиция: {max_negative_index}')
