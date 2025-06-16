from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
about_me = {
    "name": "Ivan",
    "surname": "Gulin",
    "email": "19980721qwe@gmail.com",
}

@app.route("/") # Это первый УРЛ, который будет обрабатывать
def hello_world(): # Эта функция-обработчик будет вызвана при запросе УРЛа.
    return "Hello, World!!!"


@app.route("/about")
def about():
    return about_me

if __name__ == "__main__":
    app.run(debug=True)