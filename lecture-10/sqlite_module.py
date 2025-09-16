import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, name TEXT
            )
''')
cur.execute("INSERT INTO users (name) VALUES ('Alice')")
cur.execute("INSERT INTO users (name) VALUES ('Bob')")
cur.execute("SELECT * FROM users")

conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

conn.close()