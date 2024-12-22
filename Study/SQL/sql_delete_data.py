import sqlite3

db = sqlite3.connect('test_sql.db')
cur = db.cursor()

update_params = (5,)

cur.execute("""
    DELETE FROM Students WHERE StudentsID = ?;
    """, update_params)

db.commit()
cur.close()
db.close()
