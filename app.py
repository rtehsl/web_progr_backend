from flask import Flask, url_for, redirect, render_template
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db.models import users
from flask_login import LoginManager
from db import db

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9


app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'alina_perevyazko_orm'
    db_user = 'alina_perevyazko_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}' 
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, 'alina_perevyazko_orm.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)

@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename = "404.jpg")
    style = url_for("static", filename = "lab1.css")
    return '''

<!doctype html>
<html>
<head>
    <link rel = "stylesheet" href="''' + style +'''"
</head>
    <body>
        <img src="''' + path + '''" class="full-screen-image">
    </body>
</html>
''', 404

@app.route('/')
@app.route('/index')
def index():
    style = url_for("static", filename = "lab1/lab1.css")
    return '''<!doctype html>
        <html>
        <head>
            <link rel = "stylesheet" href="''' + style +'''"
            <meta charset="UTF-8">
            <title>Перевязко Алина Юрьевна. Лабораторная работа 1</title>
        </head>
           <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
           </header>
           <body>
                <a href='/lab1'>Первая лабораторная</a>
                <br>
                <a href='/lab2'>Вторая лабораторная</a>
                <br>
                <a href='/lab3'>Третья лабораторная</a>
                 <br>
                <a href='/lab4'>Четвертая лабораторная</a>
                <br>
                <a href='/lab5'>Пятая лабораторная</a>
                <br>
                <a href='/lab6'>Шестая лабораторная</a>
                 <br>
                <a href="/lab7">Седьмая лабораторная</a>
                <br>
                <a href="/lab8">Восьмая лабораторная</a>
                <br>
                <a href="/lab9">Девятая лабораторная</a>
           </body>
           <footer>Перевязко Алина Юрьевна, ФБИ-21, 3 курс, 2024</footer>
        </html>''', 200

@app.route('/error/400')
def error_400():
    return 'Неправильный запрос', 400
@app.route('/error/401')
def error_401():
    return 'Отказ в доступе', 401
@app.route('/error/402')
def error_402():
    return 'Требуется оплата', 402
@app.route('/error/403')
def error_403():
    return 'Запрещенный', 403
@app.route('/error/405')
def error_405():
    return 'Метод не поддерживается', 405
@app.route('/error/418')
def error_418():
    return "Я не буду варить кофе, потому что я чайник", 418

@app.route('/trigger_error')
def trigger_error():
    return 1 / 0
@app.errorhandler(500)
def internal_error(error):
    return '''
<!doctype html>
<html>
    <head>
        <title>Ошибка сервера</title>
    </head>
    <body>
        <h1>Произошла ошибка на сервере</h1>
        <p>Пожалуйста, попробуйте позже.</p>
    </body>
</html>
''', 500