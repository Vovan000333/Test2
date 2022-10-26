"""
В файле run_of_60_m.txt хранятся данные о забегах школьников 6-7 классов на
60 м.

Напишите код программы, которые выполняет следующие задачи:
# 1. Для каждого школьника проставьте, оценку и сохраните результат в файл run_of_60_
mark.txt, добавив атрибут в каждую строку.
# Выведите код программы

# 2. Выведите на экран самого быстрого школьника среди мальчиков и самую быструю
школьницу среди девочек.
# Вывести ФИО, класс, результат
# Выведите код программы


Нормативы на картинке
Файл заполнить самостоятельно, в любом формате, минимум 10 строк
"""
runners=[]
with open("Задание 3.txt","r", encoding="utf-8") as myfile:
    for line in myfile:
        l = line.split()        #разделяем строку по пробелам
        # print("Бегун: ", l)
        runner  = {            #создаем словарь и присваеваем значения
            "name":l[0],
            "sex":l[1],
            "class":int(l[2]),
            "time":float(l[3])
        }
        runners.append(runner)
        # print(runners)

def bySex(x):
    return x["sex"]
def isBoy(x):
    return x["sex"] == "m"
def isGirl(x):
    return x["sex"] == "f"

def time(x):
    return x["time"]


girls = list(filter(isGirl,runners))
print(girls)

skorost = list(filter(time,runners))
print(skorost)
print("самый быстрый"+ str(skorost[-1:]))

def normativ(x):
    if runner[class] == 7 and runner[sex] == "m":
        if runner[time] > 8:\
        [ocenka]

print()