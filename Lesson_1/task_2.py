"""
    По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=nharsd2T3wsDwFsSGhpA&title=Lesson_1#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1fpqjscdcfLPImw93xwGmrf5Zm5I1F-32%26export%3Ddownload
"""

print('Введите координаты первой точки: ')
x1 = float(input('x: '))
y1 = float(input('y: '))
print('Введите координаты второй точки: ')
x2 = float(input('x: '))
y2 = float(input('y: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

if b >= 0:
    print(f'y = {k:.2f}x + {b:.2f}')
else:
    print(f'y = {k:.2f}x - {abs(b):.2f}')
