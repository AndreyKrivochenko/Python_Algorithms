"""
    Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
    1+2+...+n = n(n+1)/2, где n — любое натуральное число
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=kMc-dAgYdg5xyVbOXkTj&title=Lesson_2#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D16XIekX5LPrGtcChYSI4K3b0VL_E25oFC%26export%3Ddownload
"""

n = int(input('Введите натуральное число: '))
res = n * (n + 1) /2
sum = 0

for i in range(1, n + 1):
    sum += i

if sum == res:
    print('Равенство выполняется')
else:
    print('Равенство не выполняется')
