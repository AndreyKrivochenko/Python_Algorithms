"""
    Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
    Требуется вернуть количество различных подстрок в этой строке.
        Примечание: в сумму не включаем пустую строку и строку целиком.
        Пример работы функции:

        func("papa")
        6
        func("sova")
        9
"""
import hashlib


def func(data: str) -> int:
    count = set()
    for i in range(len(data)):
        for j in range(i, len(data)):
            spam = data[i:j + 1]
            if len(spam) < len(data) and len(spam) != 0:
                count.add(hashlib.sha1(spam.encode('utf-8')).hexdigest())
    return len(count)


print(func('papa'))
print(func('sova'))
