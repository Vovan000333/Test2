# while True:
#     x, y, z = (input("Введи интервал и степень в которую хочешь возвести, через пробел: ").split( ))
#     x, y, z = int(x), int(y), int(z)
#     if x>y:
#         x,y = y,x
#     kvadrat = list(map(lambda x: x**z, range(x, y+1)))
#     print(kvadrat)

# str  = "Привет я хочу"
# str = str.split( )
# print(str)
#
# str.append("привет")
# print(str)

# def sum(x, y):
#     c = x+y
#     print("Выполняю функцию...")
#     return c
# def calc(x):
#     c = x*2
#     print("Выполняю функцию...")
#     return c
#
# test = [1, 2, 3, 4, 5, 6]
# test2 = [1, 2, 3, 4, 5, 6]
#
# l = tuple(map(lambda x: x*2, range(1,5+1)))
#
# print(l)

# with open("/Users/vladmirmoskalevic/Documents/test.txt", "r" ) as f:
#     for line in f:
#         print(line)

"""
Задача 1: Создание нового списка
Напишите программу, которая создаёт список my_list, содержащий длины слов из списка
words (дан в начале кода), и находит сумму минимального и максимального элементов
нового списка (my_list). Результат вычислений (сумма минимального и максимального
элементов списка my_list) присвойте переменной result и выведите на экран."""

# words =["Привет", "как", "дела", "Апельсин"]
# print(list(map(len, words)))  #оптимальный способ
# my_list = []
# for i in range(len(words)):
#     x = len(words[i])
#     my_list.append(x)
#
# print(my_list)
# print(int(min(my_list))+int(max(my_list)))

"""
Задача 2: Изменение списка
Дан список numbers (содержимое списка приведено в начале кода). Найдите минимальное
(x_min) и максимальное (x_max) значения элементов данного списка.
Измените элементы списка numbers следующим образом:
если элемент является чётным числом, умножьте на x_min -в случае, если элемент
нечётный, умножьте на x_max."""

""" Блокнот """
# numbers = list(range(1,10+1))
#
# x_min = str(min(numbers))
# x_max = str(max(numbers))
#
# print(numbers)
# if i in :
#     print(n
#
#
# print(list(map(lambda x: x//2, numbers)))
#
#
# print("Максимальное значение списка: "+ str(x_max) + " и минимальное значение: "+str(x_min))

# from random import randint
#
# print("Вывод случайного целого числа ", randint(0, 9))
# print("Вывод случайного целого числа ", randrange(0, 10, 2))

notes= []
#
# # def priority(note):
# #     if note[prioryti]=="Высокий":
# #         return 0
# #     elif note[prioryti] == "Средний":
# #         return 1
# #     elif note[prioryti]=="Низкий":
# #         return 2
#
#
with open("note.txt","r", encoding="utf-8") as f:
    for line in f:
        l = line.split(',')
        note = {
            "id":int(l[0]),
            "task":l[1],
            "time":l[2],
            "date":l[3],
            "prioryti":l[4],
            "status":l[5][:-1]
        }
        notes.append(note)

print(note)


# print("{:>5} {:<5}".format("hello word", "qwerty"))

# from os import listdir
#
# for filename in listdir("/Users/vladimirmoskalevic/Desktop/Учеба Баумана")