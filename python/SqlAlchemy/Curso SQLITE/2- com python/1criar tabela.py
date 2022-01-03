import sqlite3
conn = sqlite3.connect("agenda.db")
conn.execute("CREATE TABLE IF NOT EXISTS agenda(nomes TEXT);")
conn.execute("")
conn.close()

