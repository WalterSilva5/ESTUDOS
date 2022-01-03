from time import time
from random import shuffle
from sys import setrecursionlimit

setrecursionlimit(10000)

def quicksort(v, p, r, execuções=0):
    execuções += 1
    if p < r:
        q, ex = particionar(v, p, r)
        execuções += ex

        execuções += quicksort(v, p, q - 1)  # pivotar a esquerda
        execuções += quicksort(v, q + 1, r)  # pivotar a direita

    return execuções


def particionar(v, p, r, execuções=0):
    x = v[p]  # escolhendo o pivô
    execuções += 1
    i = p
    execuções += 1
    j = p + 1
    execuções += 1
    while j <= r:
        execuções += 1
        execuções += 1
        if v[j] < x:
            i += 1
            execuções += 1
            trocar(v, i, j)  # puxando o elemento menor que o pivô
            execuções += 1  # troca
            execuções += 1  # troca
            execuções += 1  # troca
        j += 1
        execuções += 1

    trocar(v, p, i)
    execuções += 1  # troca
    execuções += 1  # troca
    execuções += 1  # troca

    return i, execuções


def trocar(v, n, m):
    temp = v[n]
    v[n] = v[m]
    v[m] = temp


def executar(entrada, caso):
    vetor = list(range(entrada))

    if caso == 'médio':
        shuffle(vetor)
    elif caso == 'pior':
        vetor.reverse()

    antes = time()
    execuções = quicksort(vetor, 0, len(vetor) - 1)
    depois = time()
    total = (depois - antes) * 1000

    print('n = {} | execuções = {} | tempo {:.2f} ms'
          .format(entrada, execuções, total))


def testes():
    print('Testes para o caso médio')
    executar(8, 'médio')
    executar(16, 'médio')
    executar(32, 'médio')
    executar(64, 'médio')
    executar(128, 'médio')
    executar(256, 'médio')
    executar(512, 'médio')
    executar(1024, 'médio')
    executar(2048, 'médio')
    executar(4096, 'médio')
    executar(8192, 'médio')
    print('=' * 60)
    print('Testes para o pior caso')
    executar(8, 'pior')
    executar(16, 'pior')
    executar(32, 'pior')
    executar(64, 'pior')
    executar(128, 'pior')
    executar(256, 'pior')
    executar(512, 'pior')
    executar(1024, 'pior')
    executar(2048, 'pior')
    executar(4096, 'pior')
    executar(8192, 'pior')
    print('=' * 60)
    print('Testes para o melhor caso')
    executar(8, 'melhor')
    executar(16, 'melhor')
    executar(32, 'melhor')
    executar(64, 'melhor')
    executar(128, 'melhor')
    executar(256, 'melhor')
    executar(512, 'melhor')
    executar(1024, 'melhor')
    executar(2048, 'melhor')
    executar(4096, 'melhor')
    executar(8192, 'melhor')
    print('=' * 60)


testes()
