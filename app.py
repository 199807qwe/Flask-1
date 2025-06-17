from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
about_me = {
    "name": "Ivan",
    "surname": "Gulin",
    "email": "19980721qwe@gmail.com",
}

quotes = [
    {
        "id": 3,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
        "id": 5,
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрые танцына только что отполированном полу людей с острыми бритвами вруках."
    },
    {
        "id": 6,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Еслибы всё работало, вас бы уволили."
    },
    {
        "id": 8,
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы. Напрактике это не так."
    },
]
# Нужно больше цитат? https://tproger.ru/devnull/programming-quotes/

@app.route("/") # Это первый УРЛ, который будет обрабатывать
def hello_world(): # Эта функция-обработчик будет вызвана при запросе УРЛа.
    return jsonify(data="Hello, World!!!")


@app.route("/about")
def about():
    return about_me

# URL: /quotes
@app.route("/quotes")
def get_quotes() -> list[dict[str, any]]:
        """Функция неявно преобразовывает список словарей в JSON"""
        return quotes

if __name__ == "__main__":
    app.run(debug=True)