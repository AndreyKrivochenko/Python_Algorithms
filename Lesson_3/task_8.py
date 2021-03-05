"""
    Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
    введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
    матрицу.
"""

SIZE_STR = 4
SIZE_COL = 4
matrix = [[int(input(f'Введите {i + 1} элемент {j + 1} строки: ')) for i in range(SIZE_COL)] for j in range(SIZE_STR)]

for i in range(SIZE_STR):
    sum_elem = 0
    for j in range(SIZE_COL):
        sum_elem += matrix[i][j]
    matrix[i].append(sum_elem)

print(*matrix, sep='\n')
