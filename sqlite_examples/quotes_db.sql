PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS quotes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT NOT NULL,
text TEXT NOT NULL
);
INSERT INTO quotes VALUES(1,'Rick Cook','Программирование сегодня — это гонка разработчиков программ...');
INSERT INTO quotes VALUES(2,'Waldi Ravens','Программирование на С похоже на быстрые танцы на только...');
INSERT INTO quotes VALUES(3,'Yoggi Berra','В теории, теория и практика неразделимы. Напрактике это не так...');
INSERT INTO quotes VALUES(4,'Mosher’s Law','Не волнуйтесь, если что-то не работает. Еслибы всё работало, вас бы уволили...');
COMMIT;
