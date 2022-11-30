from flask import Flask
from flask import request


app = Flask(__name__)

# global users
# users = {
#     "Андрей" : {"password" : "testpwd" , "money": 1000},
#     "Виктор" : {"password" : "1234" , "money": 2000}
# }

@app.route("/",methods=['GET'])
def root():
    return "<h1>Привет, я  </h1>"

@app.route("/summ/<arg1>/<arg2>",methods=['GET'])
def summ(arg1,arg2):
    print("=========================")
    print("Получаю запрос:")
    print(arg1)
    print(arg2)
    print("=========================")
    return str(int(arg1)+int(arg2))

@app.route("/prod/",methods=['GET'])
def product():
    login = request.args.get('login')
    password = request.args.get('password')
    print("=========================")
    print("Получаю запрос:")
    print(login)
    print(password)
    print("=========================")
    if password == "testpassword":
        return f"<h1>Привет,{login},<br> Заходи </h1>"
    else:
        return f"<h1>Пароль некорректный, не пущу</h1>"


@app.route("/money/",methods=['GET'])
def money():
    login = request.args.get('login')
    password = request.args.get('password')
    money = users[login]["money"]
    if password == users[login]["password"]:
        return f"<h1>Привет,{login},<br> У тебя {money} </h1>"
    else:
        return f"<h1>Пароль некорректный, не пущу</h1>"