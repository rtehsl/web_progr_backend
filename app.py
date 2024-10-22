from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("lab1/web")
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

@app.route("lab1/author")
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
               <a href="/web">web</a>
           </body>
        </html>"""

@app.route('/lab1/oak')
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
            <img src="''' + path + '''">
        </body>
</html>
'''

count = 0

@app.route('/lab1/counter')
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
@app.route('/lab1/reset_counter')
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
    app.run(debug=True)

@app.route("lab1/info")
def info():
    return redirect("lab1/author")

@app.route("/lab1/created")
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

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404