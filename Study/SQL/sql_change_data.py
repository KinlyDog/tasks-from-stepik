import sqlite3

db = sqlite3.connect('test_sql.db')
cur = db.cursor()

update_params = ('Sokolov', 5)

cur.execute("""
    UPDATE Students SET Last_name = ? WHERE StudentsID = ?;
    """, update_params)

db.commit()
cur.close()
db.close()
