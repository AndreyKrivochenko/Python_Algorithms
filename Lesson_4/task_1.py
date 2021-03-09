"""
    Определить, какое число в массиве встречается чаще всего.
"""

import random
import timeit
import cProfile


def array(min_item, max_item, size) -> list:
    arr = [random.randint(min_item, max_item) for _ in range(size)]
    return arr


# Вариант 1. Как было сделано в домашнем задании
def frequency(arr: list) -> tuple:
    count_array = [[], []]
    for _, item in enumerate(arr):
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
    return count_array[0][max_index], max_count


# Вариант 2
def frequency_2(arr: list) -> tuple:
    count_dict = {}
    for item in arr:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    max_count = 0
    max_item = 0
    for item in count_dict:
        if count_dict[item] > max_count:
            max_count = count_dict[item]
            max_item = item
    return max_item, max_count


# Вариант 3
def frequency_3(arr: list) -> tuple:
    count_dict = {}
    max_count = 0
    max_item = 0
    for item in arr:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
        if count_dict[item] > max_count:
            max_count = count_dict[item]
            max_item = item
    return max_item, max_count


# Создаём 6 массивов разной длины
a1 = array(-100, 100, 100)
a2 = array(-100, 100, 500)
a3 = array(-100, 100, 1000)
a4 = array(-100, 100, 1500)
a5 = array(-100, 100, 2000)
a6 = array(-1000, 1000, 100000)

# Замеряем производительность 1-го варианта
print(timeit.timeit('frequency(a1)', number=100, globals=globals()))    # 0.015031599999999992
print(timeit.timeit('frequency(a2)', number=100, globals=globals()))    # 0.1692755
print(timeit.timeit('frequency(a3)', number=100, globals=globals()))    # 0.41101239999999994
print(timeit.timeit('frequency(a4)', number=100, globals=globals()))    # 0.6411735000000001
print(timeit.timeit('frequency(a5)', number=100, globals=globals()))    # 0.8697240000000002

# cProfile в первом варианте запускал на а5 массиве, иначе очень долго, не дождаться... В двух других проверках
# запускал на значительно увеличенном а6 массиве, чтобы избежать нулей.
cProfile.run('frequency(a5)')
"""         2205 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.006    0.006    0.010    0.010 task_1.py:15(frequency)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
      402    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1799    0.004    0.000    0.004    0.000 {method 'index' of 'list' objects}"""


# Замеряем производительность 2-го варианта
print(timeit.timeit('frequency_2(a1)', number=100, globals=globals()))    # 0.002183000000000046
print(timeit.timeit('frequency_2(a2)', number=100, globals=globals()))    # 0.010294000000000025
print(timeit.timeit('frequency_2(a3)', number=100, globals=globals()))    # 0.020526299999999775
print(timeit.timeit('frequency_2(a4)', number=100, globals=globals()))    # 0.029832700000000045
print(timeit.timeit('frequency_2(a5)', number=100, globals=globals()))    # 0.03949109999999978
print(timeit.timeit('frequency_2(a6)', number=100, globals=globals()))    # 2.3301283

cProfile.run('frequency_2(a6)')
"""4 function calls in 0.023 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.023    0.023 <string>:1(<module>)
        1    0.023    0.023    0.023    0.023 task_1.py:35(frequency_2)
        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

# Замеряем производительность 3-го варианта
print(timeit.timeit('frequency_3(a1)', number=100, globals=globals()))    # 0.002075800000000072
print(timeit.timeit('frequency_3(a2)', number=100, globals=globals()))    # 0.012631099999999229
print(timeit.timeit('frequency_3(a3)', number=100, globals=globals()))    # 0.026445900000000577
print(timeit.timeit('frequency_3(a4)', number=100, globals=globals()))    # 0.03951919999999998
print(timeit.timeit('frequency_3(a5)', number=100, globals=globals()))    # 0.05235570000000056
print(timeit.timeit('frequency_3(a6)', number=100, globals=globals()))    # 3.218019000000001

cProfile.run('frequency_3(a6)')
"""         4 function calls in 0.033 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.033    0.033 <string>:1(<module>)
        1    0.033    0.033    0.033    0.033 task_1.py:53(frequency_3)
        1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

"""
    Замерил производительность 1-го варианта и по подсказкам cProfile понял что программу тормозят методы списков append 
    и index. Переписал функцию с использованием словаря. Во втором варианте всё стало работать сильно быстрее. Подумал, 
    а зачем мне два цикла и переписал функцию с использованием 1-го цикла и двух проверок в нём. НО программа стала 
    работать медленнее. 3-й вариант заметно отстаёт. Как мне кажется все 3 варианта линейны. Но не могу понять почему 
    два цикла с одним условием внутри каждого работают быстрее чем один цикл с двумя условиями внутри?
"""