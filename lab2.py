from flask import Blueprint, url_for, redirect, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
def example():
    name = 'Перевязко Алина'
    group = 'ФБИ-21'
    laba = '2'
    cours = '3'
    fruits = [
        { 'name': 'яблоки', 'price': 100},
        { 'name': 'груши', 'price': 120},
        { 'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 95}
    ]
    return render_template('example.html', 
                            name=name, group=group, laba=laba, 
                            cours=cours, fruits=fruits)


@lab2.route('/lab2/')
def lab22():
    return render_template('lab2.html')


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b if b != 0 else "Деление на ноль"
    pow_result = a ** b
    
    return f'''
<!doctype html>
<html>
<body>
    <h1>Результаты математических операций</h1>
    <p>Сумма: {a} + {b} = {sum_result}</p>
    <p>Разность: {a} - {b} = {sub_result}</p>
    <p>Произведение: {a} * {b} = {mul_result}</p>
    <p>Деление: {a} / {b} = {div_result}</p>
    <p>Возведение в степень: {a}<sup>{b}</sup> = {pow_result}</p>
</body>
</html>
'''


@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def calc_single_number(a):
    return redirect(url_for('calc', a=a, b=1))
books = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Научная фантастика", "pages": 328},
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Научная фантастика", "pages": 158},
    {"author": "Федор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 448},
    {"author": "Эрих Мария Ремарк", "title": "Три товарища", "genre": "Роман", "pages": 480},
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 448},
    {"author": "Антуан де Сент-Экзюпери", "title": "Маленький принц", "genre": "Философская сказка", "pages": 96},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1225},
    {"author": "Харпер Ли", "title": "Убить пересмешника", "genre": "Роман", "pages": 336}
]


@lab2.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)


@lab2.route('/laba2/a')
def a():
    return 'без слэша'


@lab2.route('/laba2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]
    

@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.lab2end(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} <p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''


@lab2.route('/lab2/add_flower/')
def add_flower_no_name():
    return "вы не задали имя цветка", 400


@lab2.route('/lab2/all_flowers')
def all_flowers():
    return f'''
<!doctype html>
<html>
<body>
    <h1>Все цветы</h1>
    <p>Всего цветов: {len(flower_list)}</p>
    <ul>
        {"".join([f"<li>{flower}</li>" for flower in flower_list])}
    </ul>
</body>
</html>
'''


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list = []
    all_flowers_link = url_for('all_flowers')
    return f'''
<!doctype html>
<html>
<body>
    <h1>Список цветов очищен</h1>
    <a href="{all_flowers_link}">Посмотреть все цветы</a>
</body>
</html>
'''
cats = [
    {"name": "Британская короткошерстная кошка", "image": "british_shorthair.jpg", "description": "Британская короткошерстная кошка — это одна из самых популярных пород кошек в мире. Она известна своей спокойной и дружелюбной натурой."},
    {"name": "Сиамская кошка", "image": "siamese.jpg", "description": "Сиамская кошка — это активная и общительная порода, известная своим голосом и яркой внешностью."},
    {"name": "Мейн-кун", "image": "maine_coon.jpg", "description": "Мейн-кун — это одна из самых крупных пород кошек, известная своей дружелюбной натурой и длинной шерстью."},
    {"name": "Рэгдолл", "image": "ragdoll.jpg", "description": "Рэгдолл — это спокойная и ласковая порода, известная своей мягкой и пушистой шерстью."},
    {"name": "Бенгальская кошка", "image": "bengal.jpg", "description": "Бенгальская кошка — это активная и любознательная порода, известная своим экзотическим внешним видом и игривой натурой."}
]


@lab2.route('/lab2/cats')
def object():
    return render_template('cats.html', cats=cats)
   