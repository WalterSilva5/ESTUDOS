1 NOT NULL
CREATE TABLE nome_tabela(
    nome_coluna tipo_coluna NOT NULL
    #EVTA QUE O NOME DA COLUNA SEJA NULL LEVANDANDO UMA EXCESSÃO
)

2 DEFAULT
CREATE TABLE nome_tabela(
    nome_coluna tipo_coluna DEFALT valor_default
    #ATRIBUI UM VALOR DEFAULT QUANDO O NOME DA COLUNA FOR NULL
)

3 UNIQUE
CREATE TABLE nome_tabela(
    nome_coluna tipo_coluna UNIQUE
    #RESTRINGE VALOR A SER O UNICO COM ESSE NOME NA TABELA
);

#EXEMPLO USANDO OS 3
####################################
CREATE TABLE AGENDA(
    NOME TEXT NOT NULL
    IDADE INT DEFAULT 1
);

INSERT INTO AGENDA(NOME, IDADE)
VALUES("JOAO", 25);
####################################

#MOSTRAR TUDO NA TABELA AGENDA
SELECT * FROM AGENDA

##RESTRIÇÃO PRIMARY KEY
4 PRIMARY KEY
    CREATE TABLE nome_tabela(
    ID"ID É O NOME" INT PRIMARY KEY NOT NULL
    NOME TEXT #outra coluna sem 5-restrições

    #EVITA A DUPLICIDADE DA COLUNA ID NA TABELA
    #A TABELA ID NÃO RECEBERA VALORES DUPLICADOS
    #COM O NOT NULL A TABELA NÃO ACEITARA VALORES NULOS
);

#auto incremento a primary key para ela não se repetir nem dar problemas

CREATE TABLE nome_tabela(
    ID INTERGER PRIMARY KEY AUTOINCREMENT NOT NULL
);

