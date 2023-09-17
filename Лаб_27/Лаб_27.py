from peewee import *

db = SqliteDatabase('bolnitsa.db')

class Employee(Model):
    name = CharField()
    post = CharField()
    pay = IntegerField()
    gender = IntegerField()

    class Meta:
        database = db

class Medicine(Model):
    name = CharField()
    doze = IntegerField()
    form = CharField()

    class Meta:
        database = db

class Ward(Model):
    number = IntegerField()
    capacity = IntegerField()
    doctor = ForeignKeyField(Employee)

    class Meta:
        database = db

class Patient(Model):
    name = CharField()
    diagnos = CharField()
    form = CharField()
    ward = ForeignKeyField(Ward)

    class Meta:
        database = db

class Prescription(Model):
    patient = ForeignKeyField(Patient)
    medicine = ForeignKeyField(Medicine)

    class Meta:
        database = db

# Create the tables

db.connect()

for dock in Employee.select():
    print(f"Name: {dock.name}, post: {dock.post}, "
          f"pay: {dock.pay}, gender: {dock.gender}")