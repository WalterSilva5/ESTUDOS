def quicksort(vetor, posicao_inicial, posicao_final):
    if posicao_inicial < posicao_final:
        pivo = particionar(vetor, posicao_inicial, posicao_final)  # escolher e colocar o pivô na posição correta
        quicksort(vetor, posicao_inicial, pivo - 1)  # pivotar a esquerda
        quicksort(vetor, pivo + 1, posicao_final)  # pivotar a direita

def particionar(vetor, posicao_inicial, posicao_final):
    pivo = vetor[posicao_inicial]  # escolhendo o pivô
    proxima_posicao = posicao_inicial
    contador = posicao_inicial + 1
    while contador <= posicao_final:
        if vetor[contador] > pivo:#so troca essa seta
            proxima_posicao += 1
            trocar(vetor, proxima_posicao, contador)  # ordenamos os elementos
        contador += 1

    trocar(vetor, posicao_inicial, proxima_posicao)#trocamos a posicao inicial pela proxima posicao antes de retornar
    return proxima_posicao


def trocar(vetor, proxima_posicao, contador):
    temp = vetor[proxima_posicao]
    vetor[proxima_posicao] = vetor[contador]
    vetor[contador] = temp

#vetor desordenado
vetor = [9,3,4,2,5,8,7,1]
print(vetor)
quicksort(vetor, 0, len(vetor)-1)
print(vetor)