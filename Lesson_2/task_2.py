"""
    Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
    цифры (4, 6 и 0) и 2 нечетные (3 и 5)
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=h-eV1Q5YzbTNFnG696q4&title=Lesson_2#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D16XIekX5LPrGtcChYSI4K3b0VL_E25oFC%26export%3Ddownload
"""

num = int(input('Введите натуральное число: '))
even_num, odd_num = 0, 0
while num > 0:
    if (num % 10) % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    num //= 10
print(f'В введённом числе чётных цифр - {even_num}, нечётных - {odd_num}')
