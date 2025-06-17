import sqlite3

select_quotes = "SELECT * FROM quotes"

# Подключение в БД
connection = sqlite3.connect("store.db")

# Создаем cursor, он позволяет делать SQL-запросы
cursor = connection.cursor()

# Выполняем запрос:
cursor.execute(select_quotes)

# Извлекаем результаты запроса
quotes = cursor.fetchall()
print(f"{quotes=}")

#quotes_db = cursor.fetchall()
#print(f"{quotes_db=}")

#keys = ("id", "author", "text")
#quotes = []
#for quote_db in quotes_db:
#    quote = dict(zip(keys, quote_db))
#    print(f'{quote = }')

# Закрыть курсор:
cursor.close()

# Закрыть соединение:
connection.close()