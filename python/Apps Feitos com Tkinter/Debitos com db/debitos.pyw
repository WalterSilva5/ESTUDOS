from datetime import datetime
import sqlite3
from tkinter import *
import pickle
import subprocess
from datetime import date
from datetime import datetime
now = datetime.now()
hj = date.today()
#import shutil
#shutil.copyfile("clientes.db", "C:\Documents and Settings\Administrador\Meus documentos\Documentos\sistema de debitos com db\copia\\")

def programa():
    global tela_principal, msg, nome_cliente_label, nome_cliente_entry,cliente, bt_ver_lista_de_debitos
    global total_debitos, bt_cliente_entrar, bt_adicionar_debitos, bt_pagar_debitos, valor_label, valor_entrada
        
    global nome_cliente_entry
    tela_principal = Tk()
    tela_principal.geometry("1100x600+0+0")
    tela_principal.title("Entrar no sistema")
    tela_principal.configure(bg="#c4d1c5")

    nome_cliente_label = Label(tela_principal, text="Nome:", bg="#c4d1c5", font=("arial",40,"bold"))
    nome_cliente_label.place(x=20, y=10)
    nome_cliente_entry = Entry(tela_principal, relief="flat",width="15", font=("arial",40,"bold"))
    nome_cliente_entry.place(x=190, y=10)
    bt_cliente_entrar = Button(tela_principal, bg="#aafff9", text="Entrar", relief="groove", font="arial 20 bold", command=testa_cliente)
    bt_cliente_entrar.place(x=650, y=15)
    
    msg = Label(tela_principal, text="", fg="blue", bg="#c4d1c5", font="andalus 40 bold ")
    msg.place(x=80, y= 180)

    valor_label = Label(tela_principal, text="Valor:", bg="#c4d1c5", font=("arial",40,"bold"))
    valor_entrada = Entry(tela_principal, relief="flat",width="15", font=("arial",40,"bold"))

    cliente = Label(tela_principal, text="teste",bg="#c4d1c5", font="Arial 20 bold")
    total_debitos = Label(tela_principal, text="",bg="#c4d1c5", relief="flat", font="Arial 20 bold")


    bt_adicionar_debitos = Button(tela_principal, text="Adicionar\nValor", bg="#0fff0f", font="arial 25 bold", command=adicionar_debito)
    bt_pagar_debitos = Button(tela_principal, text="Pagar\nValor", bg="#0fff0f", font="arial 25 bold",command = pagar_debitos)
    bt_ver_lista_de_debitos = Button(tela_principal, text="Ver Lista\nde Debitos", bg="#0fff0f", font="arial 25 bold",command = ver_lista_de_debitos)




    bt_fechar = Button(tela_principal, text="Sair", relief="groove", bg="red",
        font="Arial 30 bold", command = sair).place(x=950,y=500)

    tela_principal.mainloop()

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
        widgets_debitos()
    else:
        msg["text"]="Cliente Não Cadastrado!"

def widgets_debitos():
    global total
    total = 0

    nome_cliente_label.place(x=10000)
    nome_cliente_entry.place(x=10000)
    bt_cliente_entrar.place(x=10000)
    msg["text"]=""
    bt_adicionar_debitos.place(x=10, y=450)
    bt_pagar_debitos.place(x=200, y=450)
    bt_ver_lista_de_debitos.place(x=330, y=450)
    valor_label.place(x=25, y= 100)
    valor_entrada.place(x=185, y=100)

    conn = sqlite3.connect("clientes.db")
    debitos = conn.execute("select debitos from clientes where nomes == '{}' ".format(nome)).fetchall()
    conn.close()
    
    debitos = (str(debitos)[4:-5]).split(",")
    for debito in range(0,len(debitos),3):
        x = debitos[debito][2:-1]
        try:
            total += float(x)
        except:
            pass
    
    cliente.place(x=100,y=20)
    cliente["text"]="Cliente: {}".format(nome)


    total_debitos.place(x=100, y=50)
    total_debitos["text"]="O cliente esta devendo R$: {:.2f}".format(total)


def fechar():
    exit()
    

def sair():
    subprocess.Popen("{} {}".format("python", "debitos.py"))
    subprocess.Popen("{} {}".format("python", "enviar.py"))
    exit()
    
def adicionar_debito():
    conn = sqlite3.connect("clientes.db")
    debito_atual = str((conn.execute("select debitos from clientes where nomes == '{}'".format(nome))).fetchall())[4:-5]
    conn.close()

    try:
        novo_debito = debito_atual+"('{:.2f}','dia {}/{}/{}, as {}:{}'),".format(float(valor_entrada.get()), hj.day, hj.month, hj.year, now.hour, now.minute)
        debito = "[{})]".format(novo_debito)
    except:
        msg["text"]="O Valor deve ser um numero"
    else:
        conn = sqlite3.connect("clientes.db")
        conn.execute("update clientes set debitos = ? where nomes = ?",(debito[1:-1],nome))
        conn.commit()
        conn.close()
        adicionados()

def pagar_debitos():
    try:
        valor = float(valor_entrada.get())
    except:
        msg["text"]="O valor a pagar deve ser um numero"
    else:
        if total < valor:
            msg["text"]="O valor a pagar tem que ser\nMenor ou igual ao debito"
        else:
            msg["text"]="O Valor é um numero"        
            debito = "[('{}','dia {}/{}/{}, as {}:{}'),]".format(total-valor, hj.day, hj.month, hj.year, now.hour, now.minute)
            conn = sqlite3.connect("clientes.db")
            conn.execute("update clientes set debitos = ? where nomes = ?",(debito,nome))
            conn.commit()
            conn.close()
            removidos()

def ver_lista_de_debitos():
    conn = sqlite3.connect("clientes.db")
    debitos = str((conn.execute("select debitos from clientes where nomes = '{}'".format(nome))).fetchall())[2:-7]
    debitos = debitos.split("),(")
    conn.close()
    temp = open("temp.txt","w")
    temp.write("Lista de Debitos do cliente:\n{}\n".format(nome))
    for debito in debitos:
        temp.write(debito+"\n")
    temp.write("Total R$: {}".format(total))
    temp.close()
    subprocess.Popen("{} {}".format("notepad.exe", "temp.txt"))

def removidos():
    tela_principal.destroy()
    tela_removido = Tk()
    tela_removido.geometry("600x200+300+100")
    adicionado = Label(tela_removido, text="Valor Removido", font="arial 30 bold", fg="red").place(x=100, y=20)
    ok = Button(tela_removido, text="OK", font = "arial 30 bold", bg = "blue", command = sair).place(x=200, y=90)
    tela_removido.mainloop()

def adicionados():
    tela_principal.destroy()
    tela_adicionados = Tk()
    tela_adicionados.geometry("600x200+300+100")
    adicionado = Label(tela_adicionados, text="Valores Adicionados", font="arial 30 bold", fg="red").place(x=100, y=20)
    ok = Button(tela_adicionados, text="OK", font = "arial 30 bold", bg = "blue", command = sair).place(x=200, y=90)
    tela_adicionados.mainloop()
    

programa()
