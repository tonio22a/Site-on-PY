from flask import Flask
import random
import string

app = Flask(__name__)

facts = [
    "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
    "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
    "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
    "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
    "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ."
]

@app.route("/")
def welcome():
    return '''
        <h1>Добро пожаловать!</h1>
        <p><a href="/fact" style="text-decoration: none; color: blue;">Посмотреть факт</a></p>
        <p><a href="/pingvinchiki" style="text-decoration: none; color: blue;">Пингвинчики</a></p>
        <p><a href="/password" style="text-decoration: none; color: blue;">Генератор паролей</a></p>
    '''

@app.route("/pingvinchiki")
def pingv():
    return '''
    <h1>Пингвинчики</h1>
    '''

@app.route("/fact")
def show_fact():
    random_fact = random.choice(facts)
    return f'''
        <h1>Случайный факт:</h1>
        <p>{random_fact}</p>
        <p><a href="/fact" style="text-decoration: none; color: blue;">Сгенерировать новый факт</a></p>
        <p><a href="/" style="text-decoration: none; color: blue;">Вернуться назад</a></p>
    '''

@app.route("/password")
def generate_password():
    password_length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return f'''
        <h1>Ваш случайный пароль:</h1>
        <p style="font-size: 2em; color: green;">{password}</p>
        <p><a href="/password" style="text-decoration: none; color: blue;">Сгенерировать новый пароль</a></p>
        <p><a href="/" style="text-decoration: none; color: blue;">Вернуться назад</a></p>
    '''


app.run(debug=True)
