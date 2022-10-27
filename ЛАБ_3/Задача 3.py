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
from typing import List, Dict

runners: list[dict[str, str | int | float]]=[]
with open("run_of_60_m.txt","r", encoding="utf-8") as myfile:
    for line in myfile:
        l = line.split()        #разделяем строку по пробелам
        print("Бегун: ", l)
        runner  = {             #создаем словарь и присваеваем значения
            "name":l[0],
            "sex":l[1],
            "class":l[2],
            "time":float(l[3])
        }
        runners.append(runner)
        # print(runners)

def bySex(x):
    return x["sex"]
def isBoy(x):
    return x["sex"] == "M"
def isGirl(x):
    return x["sex"] == "F"
def time(x):
    return x["time"]
def getMarks(runner):
    if runner["class"] == "6" and runner["sex"] == "M":
        if runner["time"] <= 9.9:
            runner["mark"] = 5
            return runner
        elif runner["time"] <= 10.4:
            runner["mark"] = 4
            return runner
        elif runner["time"] <= 11.1:
            runner["mark"] = 3
            return runner
        else:
            runner["mark"] = 2
            return runner
    elif runner["class"] == "7" and runner["sex"] == "M":
        if runner["time"] <= 9.4:
            runner["mark"] = 5
            return runner
        elif runner["time"] <= 10.2:
            runner["mark"] = 4
            return runner
        elif runner["time"] <= 11.0:
            runner["mark"] = 3
            return runner
        else:
            runner["mark"] = 2
            return runner
    elif runner["class"] == "6" and runner["sex"] == "F":
        if runner["time"] <= 10.3:
            runner["mark"] = 5
            return runner
        elif runner["time"] <= 10.6:
            runner["mark"] = 4
            return runner
        elif runner["time"] <= 11.2:
            runner["mark"] = 3
            return runner
        else:
            runner["mark"] = 2
            return runner
    elif runner["class"] == "7" and runner["sex"] == "F":
        if runner["time"] <= 9.8:
            runner["mark"] = 5
            return runner
        elif runner["time"] <= 10.6:
            runner["mark"] = 4
            return runner
        elif runner["time"] <= 11.4:
            runner["mark"] = 3
            return runner
        else:
            runner["mark"] = 2
            return runner


girls = list(filter(isGirl,runners))
boys = list(filter(isBoy,runners))

print("Девочки"+("="*60))
print(*girls, sep="\n")
print("Мальчики"+"="*59)
print(*boys, sep="\n")

print(" ")
print("*"*68)
print(" ")


girls.sort(key=time)
boys.sort(key=time)
dict_girls = girls[0]
dict_boys = boys[0]

print("Самая быстрая девочка: "+
      "\n\t\tфамилия: "+ str(dict_girls['name'])+
      "\n\t\tкласс: "+ str(dict_girls['class'])+
      "\n\t\tвремя: "+ str(dict_girls['time'])
      )
print("Самый быстрый мальчик: "+
      "\n\t\tфамилия: "+ str(dict_boys['name'])+
      "\n\t\tкласс: "+ str(dict_boys['class'])+
      "\n\t\tвремя: "+ str(dict_boys['time'])
      )



runnersMarked = list(map(getMarks,runners))


with open("marked.txt","w",encoding="UTF-8") as myfile2:
    for runner in runnersMarked:
        myfile2.write("{:25}".format(" ".join([runner["name"],
                runner["sex"],
                runner["class"],
                str(runner["time"])])) +
                str("Оценка: ") +
                str(runner["mark"])+"\n")