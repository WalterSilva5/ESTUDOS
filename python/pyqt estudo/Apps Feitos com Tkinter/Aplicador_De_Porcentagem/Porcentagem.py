from tkinter import *


def Janela():
    """Janela principal do programa feita em tkinter
    onde tem as entradas de valores e impressão do resultado final"""
    global et_Quantidade, et_Valor_Quantidade, et_Porcentagem, lb_Valor_Final_Preco,lb_Erro

    tela = Tk()
    tela.title("Aplicador de Porcentagem.")

    tela.configure(bg="white")

    lb_Quantidade = Label(tela, fg="black", bg="white", text="Quantidade:", font=("arial", 20, "bold"))
    lb_Valor_Quantidade = Label(tela, bg="white", text="Valor Pago:", fg="black", font=("arial", 20, "bold"))
    lb_Porcentagem = Label(tela, bg="white", fg="black", font=("arial", 20, "bold"), text="Porcentagem:        %")
    lb_Valor_Final = Label(tela, bg="white",justify="left", fg="black", font=("arial", 20, "bold"), text="Preço\nDe Venda:")
    lb_Valor_Final_Preco = Label(tela, bg="white", fg="red", font=("arial", 70, "bold"), text="R$:00.00")
    lb_Erro = Label(tela, bg="white", fg="red",justify="left", font=("arial", 20, "bold"), text="")
    et_Quantidade = Entry(tela, bg="gray",fg="red", font=("arial", 20, "bold"), width=6)
    et_Valor_Quantidade = Entry(tela, bg="gray",fg="red", font=("arial", 20, "bold"), width=6)
    et_Porcentagem = Entry(tela, bg="gray",fg="red", font=("arial", 20, "bold"), width=3)

    bt_Aplicar = Button(tela,font=("arial", 20, "bold"), text="Aplicar", command = Aplicador)
    
    
    
    lb_Quantidade.place(x=5, y=2)
    lb_Valor_Quantidade.place(x=12, y=40)
    lb_Porcentagem.place(x=300,y=2)
    lb_Erro.place(x=10,y=200)
    et_Quantidade.place(x=180, y=2)
    et_Valor_Quantidade.place(x=180, y=40)
    et_Porcentagem.place(x=500,y=2)
    lb_Valor_Final.place(x=10,y=130)
    lb_Valor_Final_Preco.place(x=150,y=100)
    bt_Aplicar.place(x=470,y=200)


    tela.geometry("600x300+300+200")
    tela.mainloop()


def Aplicador():
    """Função que aplica a porcentagem informada no valor informado
    e retorna o valor final para a tela do programa """
    global et_Quantidade, et_Valor_Quantidade, et_Porcentagem, lb_Valor_Final_Preco,lb_Erro

    quantidade = et_Quantidade.get()
    valor_Quantidade = et_Valor_Quantidade.get()
    porcentagem = et_Porcentagem.get()
    try:
        quantidade = float(quantidade)
        valor_Quantidade = float(valor_Quantidade)
        porcentagem = float(porcentagem)

        valor_Unidade = valor_Quantidade / quantidade
        porcento = valor_Unidade / 100

        valor_Final = valor_Unidade + (porcento * porcentagem)

        lb_Valor_Final_Preco["text"] = ("R$:%.2f" % valor_Final)

        lb_Erro["text"] = ""

    except ValueError:
        lb_Erro["text"] ="ERRO!\nDIGITE APENAS NUMEROS."
    except Exception:
        lb_Erro["text"] ="OCORREU UM ERRO!"

Janela()
