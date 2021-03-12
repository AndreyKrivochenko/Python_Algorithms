"""
    Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
    каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
    наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict

firms = defaultdict(list)
firms_avg = defaultdict(list)

number_firm = int(input('Введите количество предприятий: '))
all_firm_profit = 0
for i in range(number_firm):
    print(f'{i + 1} фирма')
    name = input('Введите наименование: ')
    sum_profit = 0
    for j in range(4):
        profit = int(input(f'Введите прибыль за {j + 1} квартал: '))
        firms[name].append(profit)
        sum_profit += profit
    firms[name].append(sum_profit)
    all_firm_profit += sum_profit

avr_profit = all_firm_profit / number_firm

line = '*' * 50
print(line)
print(f'Средняя прибыль всех предприятий равна: {avr_profit:.2f}')
print(line)

for name in firms:
    if firms[name][4] < avr_profit:
        firms_avg['low'].append(name)
    else:
        firms_avg['high'].append(name)

print(f'Фирмы со средним доходом выше среднего: ', end='')
print(*firms_avg["high"], sep=', ')
print(line)
print(f'Фирмы со средним доходом ниже среднего: ', end='')
print(*firms_avg["low"], sep=', ')
