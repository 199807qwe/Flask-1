from flask import Flask, jsonify
from typing import Any
from random import choice


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


@app.route("/about") #Это статический URL
def about():
    return about_me

# URL: /quotes
@app.route("/quotes")
def get_quotes() -> list[dict[str, any]]:
        """Функция неявно преобразовывает список словарей в JSON"""
        return quotes

#@app.route("/params/<value>")
#def param_example(value: any):
#    return jsonify(param=value, param_type=str(type(value)))
#
@app.route("/params/<value>") #Это пример динамического URL
def param_example(value: str):
    return jsonify(param=value)

# URL: /quotes
@app.route("/quotes/<int:quote_id>")
def get_quote(quote_id: int) -> dict:
        """Функция возвращает цитату по значению ключа id=quote_id"""
        for quote in quotes:
            if quote["id"] == quote_id:
                return jsonify(quote), 200 # jsonify(str(quote['id']))
        return {"error": f"Quote with id={quote_id} not found"}, 404

@app.get("/quotes/count")
def quotes_count():
    """Function for task3 of Practice part 1."""
    return jsonify(count=len(quotes))


@app.route("/quotes/random", methods=["GET"])
def random_quote() -> dict:
    """Function for task4 of Practice part 1."""
    return jsonify(choice(quotes))


if __name__ == "__main__":
    app.run(debug=True)
