from flask import Flask, jsonify, request, g, abort
from typing import Any
from random import choice
from http import HTTPStatus
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).parent
path_to_db = BASE_DIR / "store.db" # <- тут путь к БД


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
KEYS = ('author','text','rating')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(path_to_db)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#about_me = {
#    "name": "Ivan",
#    "surname": "Gulin",
#    "email": "19980721qwe@gmail.com",
#}

# quotes = [
#     {
#         "id": 3,
#         "author": "Rick Cook",
#         "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает.",
#         "rating": 4
#     },
#     {
#         "id": 5,
#         "author": "Waldi Ravens",
#         "text": "Программирование на С похоже на быстрые танцына только что отполированном полу людей с острыми бритвами вруках.",
#         "rating": 3
#     },
#     {
#         "id": 6,
#         "author": "Mosher’s Law of Software Engineering",
#         "text": "Не волнуйтесь, если что-то не работает. Еслибы всё работало, вас бы уволили.",
#         "rating": 4
#     },
#     {
#         "id": 8,
#         "author": "Yoggi Berra",
#         "text": "В теории, теория и практика неразделимы. Напрактике это не так.",
#         "rating": 2
#     },
# ]
# Нужно больше цитат? https://tproger.ru/devnull/programming-quotes/

#@app.route("/") # Это первый УРЛ, который будет обрабатывать
#def hello_world(): # Эта функция-обработчик будет вызвана при запросе УРЛа.
#    return jsonify(data="Hello, World!!!")


#@app.route("/about") #Это статический URL
#def about():
#    return about_me




# URL: /quotes
@app.route("/quotes")
def get_quotes() -> list[dict[str, any]]:
        """Функция неявно преобразовывает список словарей в JSON"""
        select_quotes = "SELECT * FROM quotes"

        # Подключение в БД
        connection = sqlite3.connect("store.db")

        # Создаем cursor, он позволяет делать SQL-запросы
        cursor = get_db().cursor()

        # Выполняем запрос:
        cursor.execute(select_quotes)

        # Извлекаем результаты запроса
        quotes_db = cursor.fetchall() #get list[tuple]
        #print(f"{quotes=}")

        # Закрыть курсор:
        #cursor.close()  Из-за функци (cursor = get_db().cursor()) будет закрываться автоматически

        # Закрыть соединение:
        #connection.close()     Из-за функци (cursor = get_db().cursor()) будет закрываться автоматически
        # Подготовка данных для отправки в правильном формате
        # Необходимо выполнить преобразование: 
        # list[tuple] -> list[dict]
        keys = ("id", "author", "text", "rating")
        quotes = []
        for quote_db in quotes_db:
            quote = dict(zip(keys, quote_db))
            quotes.append(quote)
        return jsonify(quotes), 200

#@app.route("/params/<value>")
#def param_example(value: any):
#    return jsonify(param=value, param_type=str(type(value)))
#
# @app.route("/params/<value>") #Это пример динамического URL
# def param_example(value: str):
#     return jsonify(param=value)

# URL: /quotes
@app.route("/quotes/<int:quote_id>")
def get_quote(quote_id: int) -> dict:
        """Функция возвращает цитату по значению ключа id=quote_id"""
        select_quote = "SELECT * FROM quotes WHERE id = ?"
        cursor = get_db().cursor()
        cursor.execute(select_quote, (quote_id, ))
        quote_db = cursor.fetchone() #Получаем одну запись из БД
        if quote_db:
            keys = ("id", "author", "text", "rating")
            quote = dict(zip(keys, quote_db))
        # for quote in quotes:
        #     if quote["id"] == quote_id:
            return jsonify(quote), 200 # jsonify(str(quote['id']))
        return {"error": f"Quote with id={quote_id} not found"}, 404

@app.get("/quotes/count")
def quotes_count():
    """Function for task3 of Practice part 1."""
    select_count = "SELECT count(*) as count FROM quotes"
    cursor = get_db().cursor()
    cursor.execute(select_count)
    count = cursor.fetchone()
    if count:
        return jsonify(count=count[0]), 200
    abort(503) # Вернет ошибку 503 (База не доступна)


# @app.route("/quotes/random", methods=["GET"])
# def random_quote() -> dict:
#     """Function for task4 of Practice part 1."""
#     return jsonify(choice(quotes))

def generate_new_id():
    if not quotes:
        return 1
    return quotes[-1]["id"] + 1

#@app.route("/quotes", methods=['POST'])
#def create_quote():
#    data = request.json #json -> dict
#    print("data = ", data)
#    return {}, 201

#@app.route("/quotes", methods=['POST'])
#def create_quote():
#    """Функция создает овую цитату в списке."""
#    new_quote = request.json #json -> dict
#    last_quote = quotes[-1] #Последняя цитата в списке
#    new_id = last_quote["id"] + 1
#    new_quote["id"] = new_id
#    quotes.append(new_quote)
#    return jsonify(new_quote), 201

#@app.route("/quotes/<int:id>", methods=['PUT'])
@app.route("/quotes/<int:quote_id>", methods=['PUT'])
def edit_quote(quote_id):
    new_data = request.json
#    for quote in quotes:
#        if quote["id"] == id:
#            if "author" in new_data:
#                quote["author"] = new_data["author"]
#            if "text" in new_data:
#                quote["text"] = new_data["text"]
#            return jsonify(quote), 200
#    return jsonify({"error": f"Quote not found"}), 404
#    keys = ('author', 'text', 'rating')
#    if not set(new_data.keys()) - set(keys):
    if not set(new_data.keys()) - set(KEYS):
        for quote in quotes:
            if quote["id"] == quote_id:
                if "rating" in new_data and new_data['rating'] not in range(1, 6):
                    new_data.pop('rating')                   
                quote.update(new_data)
                return jsonify(quote), 200
    else:
        return jsonify(error="Send bad data to update"), 400
    return jsonify({"error": "Quote not found"}), 404




@app.route("/quotes", methods=["POST"])
def create_quote():
    new_quote = request.json
    if not set(new_quote.keys()) - set(KEYS):
        new_id = generate_new_id()
        new_quote["id"]= new_id
        new_quote["rating"] = 1
        quotes.append(new_quote)
    else:
        return jsonify(error="Send bad data to create new quote"), 400
    return jsonify(new_quote), 201


@app.route("/quotes/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id: int):
    for quote in quotes:
        if quote["id"] == quote_id:
            quotes.remove(quote)
            return jsonify({"message": f"Quote with id={quote_id} has deleted"}), 200
    return {"error": f"Quote with id={quote_id} not found"}, 404

@app.route("/quotes/filter", methods=['GET'])
def filter_quotes():
    """Поиск по фильтру"""
    author = request.args.get('author')
    rating = request.args.get('rating')
    filtered_quotes = quotes[:]
    if author:
        filtered_quotes = [quote for quote in filtered_quotes if quote['author'] == author]
    if rating:
        filtered_quotes = [quote for quote in filtered_quotes if str(quote['rating']) == rating]

    return jsonify(filtered_quotes), 200

@app.route("/quotes/filter_v2", methods=['GET'])
def filter_quotes_v2():
    """Поиск по фильтру"""
    filtered_quotes = quotes.copy()
   # Цикл по query parameters
    for key, value in request.args.items():
        result = []
        if key not in KEYS:
            return jsonify(error=f"Invalid param={value}"), 400
        if key == 'rating':
            value = int(value)
        for quote in filtered_quotes:
            if quote[key] == value:
                result.append(quote)     
        filtered_quotes = result.copy()
    return jsonify(filtered_quotes), 200
  

if __name__ == "__main__":
    app.run(debug=True)
