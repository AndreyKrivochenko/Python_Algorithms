"""
    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
    введено число 3486, надо вывести 6843
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=KCCSHO7trh1kyuBBhnnj&title=Lesson_2#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D16XIekX5LPrGtcChYSI4K3b0VL_E25oFC%26export%3Ddownload
"""


def func(a):
    if a // 10 == 0:
        return f'{a}'
    else:
        return f'{a % 10}{func(a // 10)}'


num = int(input('Введите натуральное число: '))
result = func(num)
print(f'Обратное по порядку цифр число - {int(result)}')
