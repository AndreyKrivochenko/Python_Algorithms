"""
    Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
    промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random


def merge(left, right):
    result = []
    i, j = 0, 0
    left_end, right_end = len(left), len(right)
    while i < left_end and j < right_end:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < left_end:
        result.append(left[i])
        i += 1
    while j < right_end:
        result.append(right[j])
        j += 1
    return result


def merge_sort(data):
    if len(data) < 2:
        return data
    middle = len(data) // 2
    left = merge_sort(data[0:middle])
    right = merge_sort(data[middle:len(data)])
    return merge(left, right)


array = [random.uniform(0, 49) for _ in range(10)]
print(array)
print(merge_sort(array))