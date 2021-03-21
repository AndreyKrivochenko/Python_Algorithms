"""
    Закодируйте любую строку по алгоритму Хаффмана.

    Как-то у меня получилось без деревьев... Алгоритм Хаффмана точно, но на вложенных кортежах.
    Сделал и кодировку и раскодировку.

    Спасибо вам за курс! Не смог на присутствовать на вебинарах онлайн, они у меня начинались в 12 ночи, а каждое
    утро на работу((. Благодаря вам я начинаю ощущать, что возможно что-то и получится у меня в программировании.
    Спасибо вам огромное!!!
"""
from collections import Counter


def create_table(data: str):
    count_data = Counter(data)
    while len(count_data) > 1:
        eggs = (count_data.most_common()[-2:][0][0], count_data.most_common()[-2:][1][0])
        spam = count_data.most_common()[-2:][0][1] + count_data.most_common()[-2:][1][1]
        count_data[eggs] = spam
        del count_data[count_data.most_common()[-2:][0][0]], count_data[count_data.most_common()[-2:][1][0]]
    count_data = count_data.most_common()[:1][0][0]
    return fill_table(count_data)


def fill_table(data, spam='', table_=None):
    if table_ is None:
        table_ = {}
    if len(data) == 2:
        spam += '0'
        fill_table(data[0], spam, table_)
        spam = spam[:-1]
        spam += '1'
        fill_table(data[1], spam, table_)
    else:
        table_[data] = spam
    return table_


def encode_string(data: str, enc_table: dict):
    spam = ''
    for el in data:
        spam += f'{enc_table[el]}'
    return spam


def decode_string(data: str, enc_table: dict):
    spam = ''
    i = j = 0
    while i < len(data):
        flag = True
        while flag:
            if data[i:j] in enc_table.values():
                spam += ''.join([key for key, val in enc_table.items() if val == data[i:j]])
                flag = False
                i = j
            else:
                j += 1
    return spam


st = 'It’s never too late to be what you might have been'
table_2 = create_table(st)
print(table_2)
enc_st = encode_string(st, table_2)
print(enc_st)
dec_st = decode_string(enc_st, table_2)
print(dec_st)
