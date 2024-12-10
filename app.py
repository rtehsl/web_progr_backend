from flask import Flask, url_for, redirect, render_template, session
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5

app = Flask(__name__)

app.secret_key = 'секретно-секретный секрет'

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)

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


