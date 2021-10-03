from time import time
from random import shuffle


def merge_sort(v, p, r, execuções=0):
    execuções += 1
    if p < r:
        q = (p + r) // 2
        execuções += 1
        execuções += merge_sort(v, p, q)
        execuções += merge_sort(v, q + 1, r)
        execuções += intercalar(v, p, q, r)

    return execuções


def intercalar(v, p, q, r, execuções=0):
    temp = v.copy()
    execuções += 1

    i = p  # índice do primeiro sub-vetor
    execuções += 1
    j = q + 1  # índice do segundo sub-vetor
    execuções += 1
    k = p  # índice do vetor
    execuções += 1
    while k <= r:
        execuções += 1
        execuções += 1
        if i > q:
            # primeiro sub-vetor já terminou
            # copiar todos os elementos do segundo sub-vetor
            v[k] = temp[j]
            execuções += 1
            j += 1
            execuções += 1
        elif j > r:
            # segundo sub-vetor já terminou
            # copiar todos os elementos do segundo sub-vetor
            v[k] = temp[i]
            execuções += 1
            i += 1
            execuções += 1
        elif temp[i] <= temp[j]:
            # se o elemento do primeiro sub-vetor for menor (ou igual)
            # copiar esse elemento menor (ou igual)
            v[k] = temp[i]
            execuções += 1
            i += 1
            execuções += 1
        else:
            # se o elemento do segundo sub-vetor for maior
            # copar esse elemento
            v[k] = temp[j]
            execuções += 1
            j += 1
            execuções += 1

        k += 1
        execuções += 1
    return execuções


def executar(entrada, caso):
    vetor = list(range(entrada))

    if caso == 'médio':
        shuffle(vetor)
    elif caso == 'pior':
        vetor.reverse()

    antes = time()
    execuções = merge_sort(vetor, 0, len(vetor) - 1)
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
