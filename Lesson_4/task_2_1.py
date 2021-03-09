"""
    Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
    на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

    Первый — с помощью алгоритма «Решето Эратосфена».

    Не смог придумать как правильно посчитать первоначальную длину массива n, поэтому сделал цикл увеличивающий
    длину вдвое при проверке, что необходимое нам число не входит в результирующий массив. Поэтому функция работает
    много дольше чем могла бы. Возникла мысль прикрутить меморизацию, но не успеваю придумать как. Попробую позже,
    как время появится.
"""
import timeit
import cProfile


def sieve(x: int):
    b = []
    n = x
    while len(b) < x:
        a = [0] * n  # создание массива с n количеством элементов
        for i in range(n):  # заполнение массива ...
            a[i] = i  # значениями от 0 до n-1
        a[1] = 0
        m = 2
        while m < n:  # перебор всех элементов до заданного числа
            if a[m] != 0:  # если он не равен нулю, то
                j = m * 2  # увеличить в два раза (текущий элемент - простое число)
                while j < n:
                    a[j] = 0  # заменить на 0
                    j = j + m  # перейти в позицию на m больше
            m += 1

        for i in a:
            if a[i] != 0:
                b.append(a[i])
        del a
        n *= 2
        if len(b) < x:
            b = []
    return b[x - 1]


print(timeit.timeit('sieve(100)', number=100, globals=globals()))   # 0.04028699999999999
print(timeit.timeit('sieve(200)', number=100, globals=globals()))   # 0.08320870000000002
print(timeit.timeit('sieve(300)', number=100, globals=globals()))   # 0.13006599999999996
print(timeit.timeit('sieve(400)', number=100, globals=globals()))   # 0.18695319999999999
print(timeit.timeit('sieve(500)', number=100, globals=globals()))   # 0.22611530000000002

cProfile.run('sieve(10000)')
"""
30229 function calls in 0.116 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.116    0.116 <string>:1(<module>)
        1    0.112    0.112    0.115    0.115 task_2_1.py:11(sieve)
        1    0.000    0.000    0.116    0.116 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    30214    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
