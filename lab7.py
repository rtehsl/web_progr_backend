from flask import Blueprint, render_template, request, session, current_app, abort, jsonify
from random import randint

import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path

lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def lab():
    return render_template('/lab7/lab7.html')


films = [
    {
        'title': 'Echoes of Eternity',
        'title_ru': 'Эхо вечности',
        'year': 2022,
        'description': (
            'Действие фильма происходит в фэнтезийном мире, где древние артефакты хранят '
            'тайны, способные изменить судьбу всего мира. Главный герой, молодой искатель приключений, '
            'обнаруживает древний артефакт, который дарует ему способность путешествовать во времени. '
            'Однако эта сила привлекает внимание зловещих сил, которые готовы пойти на все, '
            'чтобы завладеть артефактом. Фильм наполнен магией, сражениями и философскими размышлениями '
            'о природе времени и судьбы.'
        ),
    },
    {
        'title': 'City of Shadows',
        'title_ru': 'Город теней',
        'year': 2019,
        'description': (
            '"Город теней" - это детективный триллер, действие которого разворачивается в крупном '
            'мегаполисе, где каждый день происходят загадочные убийства. Полицейский детектив, '
            'уставший от насилия и коррупции, начинает собственное расследование, которое '
            'приводит его к мрачным тайнам города. Вместе с неожиданным союзником он сталкивается '
            'с преступным синдикатом, который управляет городом из тени. Фильм наполнен напряженными '
            'моментами, неожиданными поворотами и моральными дилеммами.'
        ),
    },
    {
        'title': 'The Star Voyager',
        'title_ru': 'Звездный странник',
        'year': 2023,
        'description': (
            '"Звездный странник" - это научно-фантастический эпос о путешествии человечества '
            'в дальние уголки Вселенной. Экипаж космического корабля отправляется в экспедицию '
            'для изучения новой планеты, которая может стать новым домом для человечества. '
            'Однако их миссия становится сложнее, когда они сталкиваются с инопланетными формами жизни '
            'и древними технологиями, которые могут изменить их представление о космосе. Фильм '
            'наполнен захватывающими космическими сражениями, философскими размышлениями о '
            'человеческой природе и удивительными визуальными эффектами.'
        ),
    }
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id >= len(films):
        return abort(404)
    else:
        return films[id]
    

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id >= len(films):
        return abort(404)
    else:
        del films[id]
        return '', 204
    

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id >= len(films):
        return abort(404)
    else:
        film = request.get_json()
        if film['description'] == '':
            return {'description': 'Заполните описание'}, 400
        films[id] = film
        return films[id]
        

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json() 
    if not film or not all(k in film for k in ('title', 'title_ru', 'year', 'description')):
        return abort(400, "Invalid film data")  
    
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    if film['title_ru'] and not film['title']:
        film['title'] = film['title_ru']
    films.append(film) 
    return {'id': len(films) - 1}, 201 