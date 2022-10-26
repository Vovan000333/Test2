"""Количество элементов в списке по заданному условию
Напишите программу, которая будет подсчитывать количество элементов в списке,
значения которых больше или равны заданному минимальному порогу и меньше
максимального.
На вход программы подается n - количество элементов списка, n_min - минимальный
порог, n_max - максимальный порог.
Для демонстрации программы напишите код для генератора списка случайных
вещественных чисел lst_random в диапазоне от -10 до 10, используя функцию uniform() из
модуля random.
"""

from random import randint
from random import uniform

n_min,n_max = (input("Вееди свой диапазон в пределах -10–10 через пробел: ")).split()
n_min,n_max = int(n_min),int(n_max)
kol = int(input("Вееди количество элементов с списке: "))

if n_min > n_max:
    n_min, n_max = n_max, n_min

lst_random = []
schet = []
schet1 = 0

for i in range(kol):
    lst_random.append(float("%.2f" % uniform(-10, 10)))

for i in lst_random:
    if n_min < i < n_max:
        schet.append("подходит")
        schet1 += 1
    else:
        schet.append("не подходит")


print("В твой диапазон попало: {} чисел".format(schet1))
print("="*len(schet)*14)
print(lst_random)
print(schet)

