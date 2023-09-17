from peewee import *

db = SqliteDatabase('Auto_Salon.db')


class owener(Model):
    name = CharField()
    date_of_purchase = DateField()
    salon = CharField()

    class Meta:
        database = db


class car(Model):
    name = CharField()
    price = IntegerField()
    production_date = DateField()
    car_owener = ForeignKeyField(owener)

    class Meta:
        database = db


db.connect()

db.drop_tables([car,owener])
db.create_tables([car,owener])




Vasiliy = owener(name="Vasiliy", date_of_purchase="02.02.2002", salon="amgmotors")
murad = owener(name="murad", date_of_purchase="02.02.2002", salon="amgmotors")

Vasiliy.save()
murad.save()


BMW = car(name="BMW",  price=100000, production_date="01.01.2000", car_owener=Vasiliy)
mersedes = car(name="mersedes",  price=200000, production_date="02.02.2002", car_owener=murad)
mersedes1 = car(name="sedes",  price=200000, production_date="02.02.2002", car_owener=murad)
mersedes2 = car(name="merses",  price=400000, production_date="02.02.2002", car_owener=Vasiliy)
mersedes3= car(name="merdes",  price=300000, production_date="02.02.2002", car_owener=murad)

BMW.save()
mersedes.save()
mersedes1.save()
mersedes2.save()
mersedes3.save()




myid = owener.get(owener.name=="Vasiliy")
print(myid)

a = car.select().where(car.car_owener==myid)
# print(a)
for i in a:
    print(i.name)

