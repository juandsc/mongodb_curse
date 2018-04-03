from bottle import route, run, debug, template, post, request, redirect, response
from pymongo import MongoClient


@route('/')
def index():
    # Connect to database
    connection = MongoClient('localhost', 27017)
    db = connection.test

    # Handles names collection
    names = db.names
    first_name = names.find_one()

    my_things = ['perro', 'gato', 'loro']

    return template('index', name=first_name['name'], things=my_things)


@post('/favorite_pet')
def favorite_fruit():
    pet = request.forms.get('pet')
    if pet is None or pet == '':
        pet = 'No pet selected'

    response.set_cookie('pet', pet)
    redirect('/show_pet')


@route('/show_pet')
def show_pet():
    pet = request.get_cookie('pet')
    return template('favorite_pet', {'pet': pet})


debug(True)
run(host='localhost', port=8080)
