from time import time
from random import shuffle


def insertion_sort(v, execuções=0):
    i = 1
    while i < len(v):
        execuções += 1
        troca = False
        execuções += 1
        temp = v[i]
        execuções += 1

        j = i - 1
        execuções += 1
        while j >= 0 and v[j] > temp:
            execuções += 1
            v[j + 1] = v[j]
            execuções += 1
            troca = True
            execuções += 1
            j -= 1
            execuções += 1

        execuções += 1
        if troca:
            execuções += 1
            v[j + 1] = temp

        i += 1
        execuções += 1

    return execuções


def executar(entrada, caso):
    vetor = list(range(entrada))

    if caso == 'médio':
        shuffle(vetor)
    elif caso == 'pior':
        vetor.reverse()

    antes = time()
    execuções = insertion_sort(vetor)
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
