import sqlite3

db = sqlite3.connect('test_sql.db')
cur = db.cursor()

drop_table = 'Student2'

# Проверка имени таблицы
if not drop_table.isidentifier():
    raise ValueError("Invalid table name")

# Удаление таблицы
cur.execute(f"DROP TABLE {drop_table};")

db.commit()
cur.close()
db.close()
