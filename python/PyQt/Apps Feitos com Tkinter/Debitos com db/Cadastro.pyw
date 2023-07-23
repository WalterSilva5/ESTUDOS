import os.path
from tkinter import *
import sqlite3
from datetime import date
from datetime import datetime
now = datetime.now()
hj = date.today()

def janela_cadastro():
    global tela_cadastro, msg_cadastro
    global nome_cliente_entry
    tela_cadastro = Tk()
    tela_cadastro.geometry("800x600+500+100")
    tela_cadastro.title("cadastrar no sistema")
    
    nome_cliente_label = Label(tela_cadastro, text="Nome:", font=("arial",40,"bold"))
    nome_cliente_label.place(x=20, y=10)
    nome_cliente_entry = Entry(tela_cadastro, relief="flat",width="15", font=("arial",40,"bold"))
    nome_cliente_entry.place(x=190, y=10)
    bt_cliente_cadastrar = Button(tela_cadastro, bg="#aafff9", text="cadastrar", relief="groove", font="arial 20 bold", command=testa_cliente)
    bt_cliente_cadastrar.place(x=650, y=15)
    
    msg_cadastro = Label(tela_cadastro, text="", fg="red", font="andalus 25 bold ")
    msg_cadastro.place(x=80, y= 100)

    bt_sair = Button(tela_cadastro, text="Sair", relief="groove", bg="red", 
        font="Arial 30 bold", command = sair).place(x=650,y=500)

    #bt_apagar_tudo = Button(tela_cadastro, text="Apagar\ntudo", relief="groove", bg="red", 
        #font="Arial 30 bold", command = apagar_tudo).place(x=150,y=450)



    tela_cadastro.mainloop()

def apagar_tudo():
    conn = sqlite3.connect("clientes.db")
    conn.execute("delete from clientes")
    conn.commit()
    conn.close()

    msg_cadastro["text"]="Tudo Apagado"

def testa_cliente():
    global nome
    nome = nome_cliente_entry.get().title()

    conn = sqlite3.connect("clientes.db")
    clientes = (str(conn.execute("SELECT nomes FROM clientes").fetchall())[1:-1]).split(", ")
    conn.close()
    existe = False
    for cliente in clientes:
        if cliente == "('{}',)".format(nome):
            existe = True
          
    if existe:
        msg_cadastro["text"]="Cliente Ja Cadastrado!"
    else:
        cadastrar()
        
def cadastrar():
    conn = sqlite3.connect("clientes.db")
    debito_inicial = "[('0','dia {}/{}/{}, as {}:{}'),]".format(hj.day, hj.month, hj.year, now.hour, now.minute
)
    print(debito_inicial)
    conn.execute("INSERT INTO clientes(nomes, debitos) values(?, ?)",(nome,debito_inicial))
    conn.commit()
    conn.close()
    msg_cadastro["text"]="CLIENTE CADASTRADO COM SUCESSO!"



def sair():
    exit()

janela_cadastro()

#C:\Documents and Settings\Administrador\Meus documentos\Documentos\sistema de debitos com db\clientes.db