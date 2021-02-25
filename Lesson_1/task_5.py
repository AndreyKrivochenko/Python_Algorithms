"""
    Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=wy9Tvztaxyfz9HBC_od8&title=Lesson_1#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1fpqjscdcfLPImw93xwGmrf5Zm5I1F-32%26export%3Ddownload
"""

print('Введите две маленькие латинские буквы')
a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')

x = ord(a) - 96
y = ord(b) - 96
z = abs(x - y) - 1

print(f'\nПервая буква стоит на {x} месте алфавита\nВторая на {y} месте\nМежду ними {z} букв')
