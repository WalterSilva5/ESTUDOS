CREATE TABLE usuarios(
    login TEXT PRIMARY KEY NOT NULL,
    senha TEXT NOT NULL
);

#deletar usuario se nome dele for joao
#tem que por aspas
delete from usuarios where login == "joao"

#buscar tudo no banco de dados
select * from usuarios

#inserir um usuario no bd 
INSERT INTO usuarios(login,senha)
	values("walter","1234");

#buscar tudo no banco de dados
select * from usuarios

#salvar oq fez durante a conexão
conn.execute(comando sql qualquer)
#salvar
conn.commit()

#quando quiser ler o valor dentro do bd tem que fatiar o retorno
retorno = retorno[2:len(retorno)-4

]