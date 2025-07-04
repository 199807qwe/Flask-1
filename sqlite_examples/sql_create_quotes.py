import sqlite3
create_quotes = """
INSERT INTO
quotes (author,text)
VALUES
('Rick Cook', 'Программирование сегодня — это гонка разработчиков программ...'),
('Waldi Ravens', 'Программирование на С похоже на быстрые танцы на только...'),
('Yoggi Berra', 'В теории, теория и практика неразделимы. Напрактике это не так...'),
('Mosher’s Law', 'Не волнуйтесь, если что-то не работает. Еслибы всё работало, вас бы уволили...');
"""
# Подключение в БД
connection = sqlite3.connect("store.db")

# Создаем cursor, он позволяет делать SQL-запросы
cursor = connection.cursor()

# Выполняем запрос:
cursor.execute(create_quotes)

# Фиксируем выполнение(транзакцию)
connection.commit()

# Закрыть курсор:
cursor.close()

# Закрыть соединение:
connection.close()