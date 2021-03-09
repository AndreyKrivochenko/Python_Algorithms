"""
    Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
    на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

    Второй — без использования «Решета Эратосфена».
"""
import timeit
import cProfile


def prime(x):
    prime_list = [2]
    temp_prime = 3
    while len(prime_list) < x:
        for i in range(2, temp_prime):
            if temp_prime % i == 0:
                break
        else:
            prime_list.append(temp_prime)
        temp_prime += 1
    return prime_list[x - 1]


print(timeit.timeit('prime(100)', number=100, globals=globals()))   # 0.1090814
print(timeit.timeit('prime(200)', number=100, globals=globals()))   # 0.5182032000000001
print(timeit.timeit('prime(300)', number=100, globals=globals()))   # 1.2633614
print(timeit.timeit('prime(400)', number=100, globals=globals()))   # 2.3833897000000004
print(timeit.timeit('prime(500)', number=100, globals=globals()))   # 3.9647323000000005

cProfile.run('prime(10000)')
"""
114731 function calls in 25.086 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   25.086   25.086 <string>:1(<module>)
        1   25.074   25.074   25.086   25.086 task_2_2.py:11(prime)
        1    0.000    0.000   25.086   25.086 {built-in method builtins.exec}
   104728    0.009    0.000    0.009    0.000 {built-in method builtins.len}
     9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
