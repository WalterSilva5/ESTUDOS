import sqlite3


conn = sqlite3.connect("usuario.db")
conn.execute("""CREATE TABLE IF NOT EXISTS usuarios(
    login TEXT PRIMARY KEY UNIQUE,
    senha TEXT UNIQUE
);""")
conn.commit()
conn.close()

conn = sqlite3.connect("usuario.db")
conn.execute("""INSERT INTO usuarios(login, senha)
    values("walter","1234")
    ;""")
conn.commit()
conn.close()


#comando seleect
#SELECT nome
#FROM agenda;


conn = sqlite3.connect("usuario.db")
sel1 = 'SELECT * FROM usuarios WHERE login == {}'
sel2 = 'SELECT * FROM usuarios WHERE login = {} and senha = {} '


def data_read(e1,e2):
    for row in conn.execute(sel1.format(e1)):
        print(row)

    print("===========")

    for row in conn.execute(sel2.format(e1, e2)):
        print(row)

data_read('walter','1234')