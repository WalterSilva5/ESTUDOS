from time import time


def busca_binaria(v, x, execuções=0):
    p = 0
    r = len(v) - 1

    while p <= r:
        execuções += 1
        q = (p + r) // 2
        execuções += 1
        execuções += 1
        if x < v[q]:
            r = q - 1
            execuções += 1
        elif x > v[q]:
            p = q + 1
            execuções += 1
        else:
            return execuções

    return execuções


def busca_sequencial(v, x, execuções=0):
    i = 0
    while i < len(v):
        execuções += 1
        execuções += 1
        if v[i] == x:
            return execuções
        i += 1
        execuções += 1

    return execuções


def busca_sequencial_sentinela(v, x, execuções=0):
    v.append(x)
    i = 0
    while v[i] != x:
        execuções += 1
        i += 1
        execuções += 1

    retorno = -1

    if i != len(v) - 1:
        retorno = i

    del v[-1]

    return execuções


def executar(função):
    print('Executando testes com a função {}'.format(função.__name__))

    entradas = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 10000, 100000, 1000000, 10000000]
    # vetor = list(range(0, entradas[-1] + 1))  # vetor do tamanho do último elemento +1

    for n in entradas:
        vetor = list(range(0, n + 1))  # vetor do tamanho de n+1
        antes = time()
        # execuções = função(vetor, 1)  # no início
        # execuções = função(vetor, n // 2)  # no meio
        execuções = função(vetor, n)  # no fim
        depois = time()
        total = (depois - antes) * 1000
        print('n = {} | execuções = {} | tempo {:.4f} ms'
              .format(n, execuções, total))

    print('=' * 60)


executar(busca_binaria)
executar(busca_sequencial)
executar(busca_sequencial_sentinela)
