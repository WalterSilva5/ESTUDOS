from time import time


def algoritmoA(n, execuções=0):
    soma = 0
    i = 1
    while i <= n:
        execuções += 1
        soma += i
        execuções += 1
        i += 1
        execuções += 1

    return execuções


def algoritmoB(n, execuções=0):
    soma = 0
    i = 1
    while i <= n:
        execuções += 1
        j = 1
        execuções += 1
        while j <= i:
            execuções += 1
            soma += 1
            execuções += 1
            j += 1
            execuções += 1
        i += 1
        execuções += 1

    return execuções


def algoritmoC(n, execuções=0):
    soma = int(n * (n + 1) / 2)
    execuções += 1

    return execuções


def executar(função):
    print('Executando testes com a função {}'.format(função.__name__))

    entradas = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 10000, 20000]

    for n in entradas:
        antes = time()
        execuções = função(n)
        depois = time()
        total = (depois - antes) * 1000
        print('n = {} | execuções = {} | tempo {:.4f} ms'
              .format(n, execuções, total))

    print('=' * 60)


executar(algoritmoA)
executar(algoritmoB)
executar(algoritmoC)
