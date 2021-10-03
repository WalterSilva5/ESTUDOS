# -*- coding: utf-8 -*-
linhas = 2
colunas = 2
matriz = []
linha_atual = 0

def cria_linha(linhas, colunas, matriz, linha_atual):
    if len(matriz)<linhas:
        matriz.append([])
        cria_coluna(linhas, colunas, matriz, linha_atual)

def cria_coluna(linhas, colunas, matriz, linha_atual):
    if len(matriz[linha_atual])<linhas:
        matriz[linha_atual].append(int(input("valor: ")))
        cria_coluna(linhas,colunas,matriz,linha_atual)
    else:
        cria_linha(linhas,colunas,matriz,linha_atual+1)

cria_linha(linhas, colunas, matriz, linha_atual)

maior = matriz[0][0]
linha_maior = matriz[0]
linha_atual = 0
cont=0

def descobre_maior(maior, matriz ,linha_maior,linha_atual,cont):
    if matriz[linha_atual][cont]>maior:
        maior = matriz[linha_atual][cont]
        linha_maior = enumerate(matriz[linha_atual])
        descobre_maior(maior, matriz ,linha_maior,linha_atual,cont+1)

    if cont == len(matriz[linha_atual]):
        descobre_maior(maior, matriz ,linha_maior,linha_atual+1,cont=0)
    if linha_atual <= len(matriz):
        print("maior = ", maior,"linha_maior",linha_maior)

descobre_maior(maior, matriz ,linha_maior,linha_atual,cont)