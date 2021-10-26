#coding = UTF-8
from tkinter import *
global tela,tela1,t_aprovado,t_solicitado

#----------------------------------------------------------------------------------------------------#

def janela1():
	global tela
	tela = Tk()
	tela.title("Verificador de CPF para o Sistema de Debitos")

	titulo_imagem = PhotoImage(file="head.png")
	titulo = Label(tela,height=250, width = 600, image = titulo_imagem)
	titulo.place(x=-50,y=-50)

	nome = Label(tela, text="Digite o CPF Do Cliente:        .         .         -", font = ("arial",20,"bold"),fg="#000080")
	nome.place(x=110,y=200)

	a1 = Entry(tela, width =3, font =("arial", 25),fg="red")
	a1.place(x=435, y=192)
	a2 = Entry(tela, width =3, font =("arial", 25),fg="red")
	a2.place(x=513, y=192)
	a3 = Entry(tela, width =3, font =("arial", 25),fg="red")
	a3.place(x=590, y=192)
	a4 = Entry(tela, width =2, font =("arial", 25),fg="red")
	a4.place(x=677, y=192)

	verifica1_image = PhotoImage(file="bt1.png")
	verifica1_bt = Button(tela, image = verifica1_image,command = desaprovado)
	verifica1_bt.place(x=250, y=270)


	verifica2_image = PhotoImage(file="bt2.png")
	verifica2_bt = Button(tela, image = verifica2_image, command = aprovado)
	verifica2_bt.place(x=370, y=270)


	tela.geometry("800x400+200+200")
	tela.mainloop()

#----------------------------------------------------------------------------------------------------#

def fechar():
	global tela1,t_aprovado,tela
	t_aprovado.destroy()


#----------------------------------------------------------------------------------------------------#

def fechar2():
	global tela1,t_aprovado,tela,t_solicitado
	t_solicitado.destroy()


#----------------------------------------------------------------------------------------------------#

def fechar3():
	global tela1,t_aprovado,tela,t_desaprovado
	t_desaprovado.destroy()


#----------------------------------------------------------------------------------------------------#

def solicitado():

	global tela2,t_aprovado,tela,t_solicitado
	t_aprovado.destroy()
	t_solicitado = Tk()
	t_solicitado.title("Cadastro Sistema de Debitos - Limite Solicitado.")


	mensagem = Label(t_solicitado, text="Limite De Debitos Solicitado Com Sucesso!\n Caso Seja Aceito Sera Enviado Uma Mensagem Para o Telefone.",fg ="#000080", font=("impact",22)).place(x=30,y=50)



	bt_voltar_img = PhotoImage(file = "voltar.png")
	bt_voltar = Button (t_solicitado, image = bt_voltar_img, command = fechar2)
	bt_voltar.place(x=20, y=170)


	t_solicitado.geometry("800x250")
	t_solicitado.mainloop()

#----------------------------------------------------------------------------------------------------#


def aprovado():
	global tela2,t_aprovado,tela
	tela.destroy()
	t_aprovado = Tk()
	t_aprovado.title("Cadastro Sistema De Debitos - Aprovado")

	titulo_imagem = PhotoImage(file="head.png")
	titulo = Label(t_aprovado,height=250, width = 600, image = titulo_imagem)
	titulo.place(x=-50,y=-50)

	mensagem = Label(t_aprovado, text= "CADASTRO APROVADO!",fg = "green", font =("Arial",35,'bold'))
	mensagem.place(x=130, y=130)


	mensagem2 = Label(t_aprovado, text= "\t\tO Limite De Debitos Aprovado Foi De R$ 100,00\n\t\tPara Solicitar Mais Limite Digite o Valor E Clique No Botão Solicitar",fg = "#000080", font =("Arial",17,"bold"))
	mensagem2.place(x=-180, y=220)


	bt_voltar_img = PhotoImage(file = "voltar.png")
	bt_voltar = Button (t_aprovado, image = bt_voltar_img, command = fechar)
	bt_voltar.place(x=20, y=330)


	et = Entry(t_aprovado, width =6, font =("Arial",39,"bold"),fg ="red")
	et.place(x=355, y=330)

	lb_rs = Label(t_aprovado,text = "R$:",font = ("Arial",35,"bold"),fg="red")
	lb_rs.place(x=270,y=330)


	bt_solicitar_img = PhotoImage(file = "solicitado.png")
	bt_solicitar = Button (t_aprovado, image = bt_solicitar_img, command = solicitado)
	bt_solicitar.place(x=587, y=328)

	lb_rs2 = Label(t_aprovado,text = "R$: 100,00",font=("Arial",30,"bold"),fg="red")
	lb_rs2.place(x=560,y=200)

	t_aprovado.geometry("800x400+200+200")
	t_aprovado.mainloop()

#----------------------------------------------------------------------------------------------------#
def desaprovado():

	global tela,t_desaprovado

	tela.destroy()

	t_desaprovado = Tk()
	t_desaprovado.configure(background='#ffccaa')
	t_desaprovado.title("Sistema de Cadastro de Debitos - O Cadastro Não Foi Aprovado!")

	aviso = Label(t_desaprovado, text= "AVISO!",fg = "red",bg="#ffccaa", font =("Arial",65,'bold'))
	aviso.place(x=250, y=0)

	mensagem = Label(t_desaprovado, text= "CADASTRO NÃO FOI APROVADO!",fg = "red",bg='#ffccaa', font =("Arial",35,'bold'))
	mensagem.place(x=10, y=100)

	mensagem2 = Label(t_desaprovado, text ="PODEM HAVER DEBITOS ANTERIORES\nCONSTANDO NESSE CPF EM OUTRAS LOJAS\nOU ALGUM ERRO OCORREU DURANTE A VERIFICAÇÃO\nTENTE NOVAMENTE EM ALGUNS DIAS.",fg = "blue",bg="#ffccaa",font =("Arial",21,'bold'))
	mensagem2.place(x=20,y=160)

	bt_voltar_img = PhotoImage(file = "voltar.png")
	bt_voltar = Button (t_desaprovado, image = bt_voltar_img, command = fechar3)
	bt_voltar.place(x=20, y=330)



	t_desaprovado.geometry("800x400+200+200")	
	t_desaprovado.mainloop()

#----------------------------------------------------------------------------------------------------#

janela1()
