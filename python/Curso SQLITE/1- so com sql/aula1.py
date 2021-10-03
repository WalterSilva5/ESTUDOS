import sqlite3
conn = sqlite3.connect("c:/sqlite/aula/bd_estudo.db")
cursor = conn.execute('select * from estados')
rows = cursor.fetchall()
