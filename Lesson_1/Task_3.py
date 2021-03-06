"""
Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить).
Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

import random


def gen(start, finish):
    spisok = []
    slovar = {}
    for _ in range(10):
        rnd = int((finish - start) * random.random() + start)
        spisok.append(rnd)
        slovar.update({'elem_{}'.format(rnd): rnd})

    return (spisok, slovar)