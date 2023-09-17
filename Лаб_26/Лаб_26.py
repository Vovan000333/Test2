from peewee import *

db = SqliteDatabase('Restaurant.db')


class Restaurant(Model):
    name = CharField()
    pleace = CharField()
    rating = IntegerField()
    income = IntegerField()

    class Meta:
        database = db


class Product(Model):
    name = CharField()
    weight = IntegerField()
    cal = IntegerField()
    price = IntegerField()

    class Meta:
        database = db


class Employee(Model):
    Restaurant = ForeignKeyField(Restaurant)
    name = CharField()
    salary = IntegerField()
    task = CharField()

    class Meta:
        database = db


class Assortiment(Model):
    Restaurant = ForeignKeyField(Restaurant)
    product = ForeignKeyField(Product)

    class Meta:
        database = db


db.connect()

db.drop_tables([Product, Restaurant, Employee, Assortiment])
db.create_tables([Product, Restaurant, Employee, Assortiment])

Restaurant = Restaurant(name='Кафе', pleace='Baumanskaya', rating=2, income=20000)
yourname = Restaurant(name='Ваше имя', pleace='Old Arbat', rating=3, income=45000)
cofeich = Restaurant(name='Кофеич', pleace='Reutov', rating=1, income=100000)

Restaurant.save()
yourname.save()
cofeich.save()

americanoBig = Product(name='Американо Большой', weight=300, cal=15, price=180)
americanoSmall = Product(name='Американо Маленький', weight=150, cal=7, price=90)

capuchSmall = Product(name='Каппучино Маленький', weight=150, cal=20, price=150)
capuchBig = Product(name='Каппучино Большой', weight=300, cal=40, price=250)

cucumber = Product(name='Огруцовый магнат', weight=500, cal=10, price=20)

americanoBig.save()
americanoSmall.save()
capuchSmall.save()
capuchBig.save()
cucumber.save()

am_b_yourname = Assortiment(Restaurant=yourname, product=americanoBig)
am_s_yourname = Assortiment(Restaurant=yourname, product=americanoSmall)
am_b_Restaurant = Assortiment(Restaurant=Restaurant, product=americanoBig)
cap_b_Restaurant = Assortiment(Restaurant=Restaurant, product=capuchBig)
cap_s_Restaurant = Assortiment(Restaurant=Restaurant, product=capuchSmall)
cap_s_yourname = Assortiment(Restaurant=yourname, product=capuchSmall)
cu_cofeich = Assortiment(Restaurant=cofeich, product=cucumber)
am_b_yourname.save()
am_s_yourname.save()
am_b_Restaurant.save()
cap_s_Restaurant.save()
cap_b_Restaurant.save()
cap_s_yourname.save()
cu_cofeich.save()