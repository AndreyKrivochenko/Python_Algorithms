"""
    Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=ynGBpok5-9tkH1AY5TeH&title=Lesson_1#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1fpqjscdcfLPImw93xwGmrf5Zm5I1F-32%26export%3Ddownload
"""

print('Введите три разных числа')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if b < a < c or c < a < b:
    print(f'Среднее число - {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число - {b}')
else:
    print(f'Среднее число - {c}')
