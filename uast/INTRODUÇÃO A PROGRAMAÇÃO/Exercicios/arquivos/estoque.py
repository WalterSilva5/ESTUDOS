import sqlite3

def programa():
    print("Gestor de Estoque")
    print("0 sair do programa")
    print("1 Cadastrar Produto")
    print("2 Alterar Produto")
    print("3 Buscar Produto")
    print("4 Vender Produto")

    try:
        op = int(input("Digite a opção: "))
    except:
        print("Digite uma opção valida")
        programa()

    if op == 0:
        exit()
    elif op == 1:
        cadastra()
    elif op == 2:
        altera()
    elif op == 3:
        mostra()
    elif op == 4:
        vender()


def existe(codigo):
    conn = sqlite3.connect("banco.db")
    produtos = (conn.execute("SELECT * FROM produtos")).fetchall()
    for produto in produtos:
        if produto[0]==codigo:
            return True
    return False

def vender():
    codigo = int(input("Digite o codigo do produto: "))
    if existe(codigo):
        venda(codigo)
    else:
        print("O Produto não esta cadastrado\n")
def venda(codigo):
    quantidade_venda = int(input("Digite a quantidade que deseja vender: "))
    conn = sqlite3.connect("banco.db")
    quantidade = ((conn.execute("SELECT quantidade FROM produtos WHERE codigo = {}".format(codigo))).fetchall())[0][0]

    if quantidade_venda> quantidade:
        print("A quantidade em estoque é inferior a da venda\ntente novamente\n")
        programa()
    else:
        conn.execute("UPDATE produtos SET quantidade = {} WHERE codigo = {}".format(quantidade-quantidade_venda, codigo))
        print("Venda Concluida\n")
    conn.commit()
    conn.close()
    programa()
def altera():
    codigo = int(input("Digite o codigo do produto: "))
    if existe(codigo):
        alterar(codigo)
    else:
        print("O Produto não esta cadastrado\n")

def alterar(codigo):
    conn = sqlite3.connect("banco.db")
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: \n\n"))


    conn.execute("""UPDATE produtos
        SET nome = '{}', quantidade = {}, preco = {}
        WHERE codigo = {};
    """.format(nome, quantidade, preco, codigo))


    conn.commit()
    conn.close()
    programa()

def mostra():
    codigo = int(input("Digite o codigo do produto: "))
    if existe(codigo):
        mostrar(codigo)
    else:
        print("O Produto não esta cadastrado\n")
        programa()

def mostrar(codigo):
    conn = sqlite3.connect("banco.db")
    produtos = (conn.execute("SELECT * FROM produtos")).fetchall()
    codigo, nome, quantidade, preco = produtos[0]

    print("\n\nCodigo = {}\nnome = {}\nQuantidade = {}\nPreço = {}\n".format(codigo, nome, quantidade, preco))
    programa()

def cadastra():
    codigo = int(input("\nCodigo: "))
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    salva(codigo, nome, quantidade, preco)

def salva(codigo, nome, quantidade, preco):
    conn = sqlite3.connect("banco.db")
    try:
        conn.execute("INSERT INTO produtos(codigo, nome, quantidade, preco) values('{}', '{}', '{}', '{}')".format(
            codigo, nome, quantidade, preco, ))

    except:
        print("Ocorreu um erro ao cadastrar\n\n")
    else:
        print("Produto Cadastrado\n\n")
    conn.commit()
    conn.close()


    programa()


if __name__=="__main__":
    conn = sqlite3.connect("banco.db")

    conn.execute("""CREATE TABLE IF NOT EXISTS produtos(
    codigo INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco  TEXT NOT NULL
    )""")


    conn.commit()
    conn.close()

    programa()

