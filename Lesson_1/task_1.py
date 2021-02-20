""" Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson_1#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1fpqjscdcfLPImw93xwGmrf5Zm5I1F-32%26export%3Ddownload
"""
x = int(input('Введите целое трёхзначное число: '))

a = x % 10
b = (x // 10) % 10
c = x // 100

total = a + b + c
mult = a * b * c

print(f'Сумма равна {total}, произведение равно {mult}')
