"""Дан словарь с результатами жеребьевки футбольных команд по группам. Напишите код,
выполняющий следующие задачи:
foot_dict = {
'Россия': 'A',
'Португалия': 'B',
'Франция': 'C',
'Дания': 'C',
'Египет': 'A'
}
# 1. Добавьте новое значение страна 'Турция', группа B

# 2. Выведите на экран страны, попавшие в группу, название которой вводится с клавиат
уры

# 3. Посчитайте и выведите на экран количество команд в каждой группе
"""

x = input("Введи группу стран: ")
foot_dict = { 'Россия': 'A','Португалия': 'B','Франция': 'C','Дания': 'C','Египет': 'A'}
foot_dict.update({'Турция': 'B'})
grup = []
val = list(foot_dict.values())

for k, v in foot_dict.items(): #попали или нет
    if v == x:
        grup.append(k)

for i in range(len(set(val))):
    print("Количество стран в группе "+str(val[i])+" равно: "+str(val.count(val[i])))
print("="*36)
if len(grup) > 0:
    print('Страны, попавшие в веденную группу:')
    print(*grup, sep=", ")
else:
    print("Нет ниодной страны, из введеной группы")