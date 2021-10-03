#pra o algoritmo funcionar o vetor deve estar ordenado

import random 

def buscaBinaria(vetor, posicaoInicial, posicaoFinal, alvo):
    #condicao de parada da busca 
    if posicaoInicial<=posicaoFinal:
        meio=(posicaoInicial+posicaoFinal)//2
        if alvo>vetor[meio]:
            return buscaBinaria(vetor, meio+1, posicaoFinal, alvo)
        elif alvo<vetor[meio]:
            return buscaBinaria(vetor, posicaoInicial, meio-1, alvo)
        else:
            return meio
    return -1
vetor = list(range(10))
alvo = 9
resutaldo=buscaBinaria(vetor, 0, len(vetor), alvo)

print(resutaldo)
