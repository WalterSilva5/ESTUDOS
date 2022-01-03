import sqlite3
#codigo sql
INSERT INTO nome_tabela(
    coluna1,
    coluna2,
    coluna3,
);

#ex:
#agenda é o nome da tabela

INSERT INTO agenda(nome_coluna)
VALUES("joao");

INSERT INTO agenda(nome_coluna)
VALUES("maria")

INSERT INTO agenda(nome_coluna)
VALUES("jose")


#2 valores
INSERT INTO usuarios(login, senha)
VALUES("joao", "1234");

#inserir varios valores dinamicamente
c.execute("""
    INSERT INTO usuarios(login,senha)VALUES(?,?)
    ("walter", "1234")
""")