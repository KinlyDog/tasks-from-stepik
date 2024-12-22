import sqlite3

# Подключение к существующей БД
db = sqlite3.connect(r'c:\Program Files\DB Browser for SQLite\qa_testing.db')
cur = db.cursor()

cur.execute("""SELECT * FROM Students;""")

result_one = cur.fetchone()
result_one2 = cur.fetchone()
result_many = cur.fetchmany(1)
result_all = cur.fetchall()

print(result_one)
print(result_one2)
print(result_many)
print(result_all)