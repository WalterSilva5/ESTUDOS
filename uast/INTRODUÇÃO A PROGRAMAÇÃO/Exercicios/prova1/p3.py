#@author = walter pereira da silva lira
from random import randrange
linhas = 3
colunas = 6
matriz = []
conta_linhas = 0
conta_colunas = 0
linha_atual=0

"""parte que cria a matriz"""
def cria_coluna(linhas,colunas,conta_linhas,conta_colunas,linha_atual):
    if len(matriz[linha_atual])<colunas:
        matriz[linha_atual].append(randrange(999))
        cria_coluna(linhas,colunas,conta_linhas,conta_colunas,linha_atual)
    else:
        cria_linha(linhas,colunas,conta_linhas,conta_colunas,linha_atual+1)

def cria_linha(linhas,colunas,conta_linhas,conta_colunas,linha_atual):
    if len(matriz)<linhas:
        matriz.append([])
        cria_coluna(linhas,colunas,conta_linhas,conta_colunas,linha_atual)
    else:
        menor = matriz[0][0]
        posição = "0"
        linha_do_menor = matriz[0]
        linha_atual = 0
        elemento = 0
        testa_linha(matriz,menor,posição,linha_do_menor, linha_atual, elemento)

"""parte que verifica o menor valor da matriz"""
def testa_coluna(matriz, menor, posição, linha_do_menor, linha_atual, elemento):
    if elemento < len(matriz[0]):
        if menor > matriz[linha_atual][elemento]:
            menor = matriz[linha_atual][elemento]
            linha_do_menor = matriz[linha_atual]
            #somei um as posições para ficar mais facil a identificação no console
            posição ="{}x{}".format(linha_atual+1,elemento+1)
        testa_coluna(matriz, menor, posição, linha_do_menor, linha_atual, elemento+1)
    else:
        testa_linha(matriz, menor, posição, linha_do_menor, linha_atual+1, elemento)


def testa_linha(matriz, menor, posição, linha_do_menor, linha_atual, elemento):
    if linha_atual <len(matriz):
        testa_coluna(matriz, menor, posição, linha_do_menor, linha_atual, elemento=0)
    else:
        divisores=0
        contador = 1
        print("\no menor elemento é {}, sua posição é {}".format(menor,posição))
        verifica_primo(menor,divisores,contador,posição, linha_do_menor, linha_atual)
        print("\n")
        mostra(matriz,linha=0,coluna=0)

"""parte que verifica se o numero é primo"""
def verifica_primo(menor,divisores,contador,posição, linha_do_menor, linha_atual):

    if contador<=menor:
        if menor%contador == 0:
            divisores+=1
        verifica_primo(menor,divisores,contador+1,posição, linha_do_menor, linha_atual)
    else:
        mostra_resultado(divisores,menor,posição, linha_do_menor, linha_atual)

"""mostra se e primo"""
def mostra_resultado(divisores,menor,posição, linha_do_menor, linha_atual):
    if divisores == 2:
        print("{} é um numero primo".format(menor))
    else:
        print("{} não é um numero primo".format(menor))


"""mostra a matriz formatada"""
def mostra(matriz, linha,coluna):
    if linha<len(matriz):
        mostra_coluna(matriz,linha,coluna)

def mostra_coluna(matriz,linha,coluna):
    if coluna<len(matriz[0]):
        print("{}, ".format(matriz[linha][coluna]),end ="")
        mostra_coluna(matriz,linha,coluna+1)
    else:
        print("")
        mostra(matriz,linha+1,coluna=0)

"""chamada da função principal"""
cria_linha(linhas,colunas,conta_linhas,conta_colunas,linha_atual)
