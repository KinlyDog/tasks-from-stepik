import sqlite3

# Создание новой БД
db = sqlite3.connect('test_sql.db')
cur = db.cursor() # переменная для управления БД

# Создание таблицы
cur.execute("""CREATE TABLE IF NOT EXISTS Students(
    StudentsID INTEGER PRIMARY KEY,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL);""")

db.commit() # сохранение запроса

# # НЕБЕЗОПАСНЫЙ СПОСОБ - Заполнение таблицы
# cur.execute("""
#     INSERT INTO Students(First_name, Last_name)
#     VALUES('Petr', 'Petrov');""")
#
# db.commit()

# data_students = ('Semen', 'Semenov')

data_students = [('Andrey', 'Andreev'), ('Sergey', 'Sergeev')]
cur.executemany("""INSERT INTO Students(First_name, Last_name)
    VALUES (?, ?);""", data_students)
db.commit()
db.close()
