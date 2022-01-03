# -*- coding: utf-8 -*-
#
limite = 3
lista = []
def cria(lista, limite):
    if len(lista)<=limite:
        lista.append(int(input("Valor: ")))
        cria(lista,limite)
    else:
        print(lista)

cria(lista,limite)

maior = lista[0]
cont = 0


def mostra(maior):
    print(maior)
    exit()

def verifica(lista,cont,maior):
    if cont == len(lista):
        mostra( maior)
    if lista[cont]>=maior:
        maior = lista[cont]
        verifica(lista, cont + 1, maior)

verifica(lista,cont,maior)
