import sqlite3

class Animal:
    def __init__(self, index, name, kind, weight, age, keeper, home):
        self.index = index
        self.name = name
        self.kind = kind
        self.weight = weight
        self.age = age
        self.keeper = keeper
        self.home = home

    def __repr__(self):
        return ("Animal: " +
                "\n index: " + str(self.index)
                + "\n name: " + self.name
                + "\n kind: " + self.kind
                + "\n weight: " + str(self.weight)
                + "\n age: " + str(self.age)
                + "\n keeper: " + str(self.keeper)
                + "\n home: " + str(self.home))

class Employee:
    def __init__(self, index, name, task, salary):
        self.index = index
        self.name = name
        self.task = task
        self.salary = salary

    def __repr__(self):
        return ("Employee: " +
                "\n index: " + str(self.index)
                + "\n name: " + self.name
                + "\n task: " + self.task
                + "\n salary: " + str(self.salary))
animals = []
employees = []
avials = []

borya = Animal(0,"Borya","bear",300,20,1,1)
gosha = Animal(1,"Gosha","lion",150,10,2,2)
misha = Animal(2,"Misha","eagle",20,5,1,3)

animals.append(borya)
animals.append(gosha)
animals.append(misha)

victor = Employee(0,"Victor Petrov","feed",50000)
leonid = Employee(1,"Leonid ","clean",45000)

employees = [victor,leonid]

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

sqlcommand = f'''INSERT OR IGNORE INTO animals(
        id, name, home) VALUES(
        '{misha.index}',
        '{misha.name}',
        '{misha.home}'
)'''

cursor.execute(sqlcommand)

conn.commit()

cursor.execute("SELECT * FROM animals")

r = cursor.fetchall()
print(r)
