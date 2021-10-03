import sqlite3
conn = sqlite3.connect("agenda.db")
conn.execute("INSERT INTO agenda(coluna1 TEXT);")
conn.close()
