import sqlite3

db = sqlite3.connect('test_sql.db')
cur = db.cursor()

data_students = ('Semen', 'Semenov')

cur.executescript("""
    CREATE TABLE IF NOT EXISTS Student2(
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL);
    
    INSERT INTO Student2(FirstName, LastName)
    VALUES ('Andrey', 'Andreev');
    """)

db.commit()
cur.close()
db.close()