"""
    Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
    вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
    вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если
    пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
    запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он
    ввел его в качестве делителя
    Блок-схема - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Lesson_2#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D16XIekX5LPrGtcChYSI4K3b0VL_E25oFC%26export%3Ddownload
"""

znak = '+'
while znak != '0':
    num_1 = float(input('Введите первое число: '))
    znak = input('Введите знак операции: ')
    num_2 = float(input('Введите второе число: '))

    if znak == '/' and num_2 == 0:
        print('На ноль делить нельзя')
    elif znak == '+':
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
    elif znak == '-':
        print(f'{num_1} - {num_2} = {num_1 - num_2}')
    elif znak == '*':
        print(f'{num_1} * {num_2} = {num_1 * num_2}')
    elif znak == '/':
        print(f'{num_1} / {num_2} = {num_1 / num_2}')
    elif znak != '0':
        print('Введен неправильный знак операции')
