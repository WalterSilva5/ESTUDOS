import random
def buscaSeqSent(vetor, elemento):
    posicao = 0
    vetor.append(elemento)
    while vetor[posicao] != elemento:
        posicao +=1
        
    if posicao == len(vetor)-1:
        return -1

    return posicao


vetor = list(range(20))
random.shuffle(vetor)
elemento = 13

print(buscaSeqSent(vetor, elemento))
