from flask import Blueprint, url_for, redirect
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask<h1>
               <a href="/author">author</a>
           </body>
        </html>""", 200, {
            "X-Server": "sample",
            "Content-Type": "text/plain; charset=utf-8"
            }


@lab1.route("/lab1/author")
def author():
    name = "Перевязко Алина Юрьевна"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
           <body>
               <p>Студент: """ + name + """</p>
               <p>Группа: """ + group + """</p>
               <p>Факультет: """ + faculty + """</p>
               <a href="/lab1/web">web</a>
           </body>
        </html>"""


@lab1.route('/lab1/oak')
def oak ():
    path = url_for("static", filename="oak.jpg")
    style = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
    <link href="''' + style + '''" rel="stylesheet">
    </head>
        <body>
            <h1>Дуб</h1>
            <img src="''' + path + '''" class="oak-image">
        </body>
</html>
'''


count = 0


@lab1.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
         <br>
        <a href="/lab1/reset_counter">Очистить счётчик</a>
    </body>
</html>
'''


@lab1.route('/lab1/reset_counter')
def reset_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        Счётчик очищен.
        <br>
        <a href="/lab1/counter">Вернуться к счётчику</a>
    </body>
</html>
'''

if __name__ == '__main__':
    lab1.run(debug=True)


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Созданы успешно</h1>
        <div><i>что-то создано...<i><div>
    </body>
</html>
''', 201


@lab1.route('/lab1')
def lab():
    style = url_for("static", filename = "lab1.css")
    return '''<!doctype html>
        <html>
        <head>
            <link rel = "stylesheet" href="''' + style +'''"
            <title>Лабораторная 1</title>
        </head>
           <body>
                <p>
                    Flask — фреймворк для создания веб-приложений на языке
                    программирования Python, использующий набор инструментов
                    Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                    называемых микрофреймворков — минималистичных каркасов
                    веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
                </p>
                <h2>Список роутов</h2>
                <ul>
                    <li><a href="/">Главная страница</a></li>
                    <li><a href="/index">Главная страница (index)</a></li>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                    <li><a href="/lab1/web">Web</a></li>
                    <li><a href="/lab1/author">Автор</a></li>
                    <li><a href="/lab1/oak">Дуб</a></li>
                    <li><a href="/lab1/counter">Счетчик</a></li>
                    <li><a href="/lab1/reset_counter">Сброс счетчика</a></li>
                    <li><a href="/lab1/info">Информация</a></li>
                    <li><a href="/lab1/created">Создано успешно</a></li>
                    <li><a href="/error/400">Ошибка 400</a></li>
                    <li><a href="/error/401">Ошибка 401</a></li>
                    <li><a href="/error/402">Ошибка 402</a></li>
                    <li><a href="/error/403">Ошибка 403</a></li>
                    <li><a href="/error/405">Ошибка 405</a></li>
                    <li><a href="/error/418">Ошибка 418</a></li>
                    <li><a href="/trigger_error">Триггер ошибки</a></li>
                    <li><a href="/anna">Анна Асти</a></li>
                </ul>
           </body>
           <footer>Перевязко Алина Юрьевна, ФБИ-22, 3 курс, 2024</footer>
        </html>''', 200


@lab1.route('/lab1/anna')
def anna():
    path = url_for("static", filename = "anna.jpg")
    style = url_for("static", filename = "lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel = "stylesheet" href="''' + style +'''"
        <meta charset="UTF-8">
        <title>Царица</title>
    </head>
    <body>
        <h1>Царица</h1>
        <p>
            Все твои романы — тяжёлый вид спорта
        </p>
        <p>
            Каждый бывший выводил из зоны комфорта
        </p>
        <p>
            Каждый бывший — тренер личностного роста
        </p>
        <p>
            Ты стала хитрее, детка стала взрослой
        </p>
        <img src="''' + path + '''" alt="anna">
    </body>
</html>
''', 200, {
    'Content-Language': 'ru',
    'X-Custom-Header-1': 'Anna',
    'X-Custom-Header-2': 'Asti'
}