import sqlite3

# Подключение к существующей БД
db = sqlite3.connect(r'c:\Program Files\DB Browser for SQLite\qa_testing.db')
cur = db.cursor()

cur.execute("""SELECT * FROM Students;""")
result = cur.fetchall()

print(result)