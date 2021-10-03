#conexão simples
import sqlite3
#guardamos a conexão na variavel conn
conn = sqlite3.connect('teste.db')
#fechamos a conexão
conn.close()
