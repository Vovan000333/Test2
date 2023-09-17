# Написать свою БД и реализовать выбор и тд

import sqlite3

class car:
    def __init__(self, ID, brand, year, weight, name_of_owener, date_of_TO):
        self.ID = ID
        self.brand = brand
        self.year = year
        self.weight = weight
        self.name_of_owener = name_of_owener
        self.date_of_TO = date_of_TO

    def __repr__(self):
        return ("Animal: " +
                "\n ID: " + str(self.ID)
                + "\n brand: " + self.brand
                + "\n year: " + str(self.year)
                + "\n weight: " + str(self.weight)
                + "\n owener: " + self.owener
                + "\n TO: " + str(self.TO)

class owener:
    def __init__(self, ID, name, name_car, date_of_buy):
        self.ID = ID
        self.name = name
        self.name_car = name_car
        self.date_of_buy = date_of_buy

    def __repr__(self):
        return ("Employee: " +
                "\n ID: " + str(self.ID)
                + "\n name: " + self.name
                + "\n name_car: " + self.name_car
                + "\n date_of_buy: " + str(self.date_of_buy))

class salon:
    def __init__(self, ID, place, kol_car, kol_owener):
        self.ID = ID
        self.place = place
        self.kol_car = kol_car
        self.kol_owener = kol_owener

    def __repr__(self):
        return ("Avial: " +
                "\n ID: " + str(self.ID)
                + "\n place: " + self.place
                + "\n kol_car: " + str(self.kol_car)
                + "\n kol_owener: " + str(self.kol_owener))
animals = []
employees = []
avials = []

borya = Animal(1,"Borya","bear",300,20,1,1)
gosha = Animal(2,"Gosha","lion",150,10,2,2)
misha = Animal(3,"Misha","eagle",20,5,1,3)

animals.append(borya)
animals.append(gosha)
animals.append(misha)

victor = Employee(1,"Victor Petrov","feed",50000)
leonid = Employee(2,"Leonid ","clean",45000)

employee = [victor,leonid]

tundra = Avial(1,"Bearlodge","tundra",200)
desert = Avial(2,"sahara","desert",150)
forest = Avial(3,"moscow","forest",50)

avial = [tundra,desert,forest]


conn = sqlite3.connect("my.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS animals(
            id INT PRIMARY KEY,
            name TEXT,
            kind TEXT,
            weight REAL,
            age INT,
            keeper INT,
            home INT
            )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS employee(
            id INT PRIMARY KEY,
            name TEXT,
            task TEXT,
            salary INT
            )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS avial(
            id INT PRIMARY KEY,
            name TEXT,
            biome TEXT,
            size INT
            )''')

for a in animals:
    sqlcommand = f'''INSERT OR IGNORE INTO animals(
             id, name, kind, weight, age, keeper, home) VALUES(
            '{a.index}',
            '{a.name}',
            '{a.kind}',
            '{a.weight}',
            '{a.age}',
            '{a.keeper}',
            '{a.home}'
            )'''
    cursor.execute(sqlcommand)

for a in employee:
    sqlcommand = f'''INSERT OR IGNORE INTO employee(
             id, name, task, salary) VALUES(
            '{a.index}',
            '{a.name}',
            '{a.task}',
            '{a.salary}'
            )'''
    cursor.execute(sqlcommand)

for a in avial:
    sqlcommand = f'''INSERT OR IGNORE INTO avial(
             id, name, biome, size) VALUES(
            '{a.index}',
            '{a.name}',
            '{a.biome}',
            '{a.size}'
            )'''
    cursor.execute(sqlcommand)

conn.commit()
