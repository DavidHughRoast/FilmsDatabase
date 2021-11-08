import sqlite3
conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()


def printf():
    for row in cursor.execute("select * from tblFilms"):
        print(row)
