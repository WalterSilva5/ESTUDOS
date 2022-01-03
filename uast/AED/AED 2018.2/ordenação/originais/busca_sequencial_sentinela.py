from time import time


def busca_sequencial_sentinela(v, x):
    v.append(x)
    i = 0
    while v[i] != x:
        i += 1

    retorno = -1

    if i != len(v) - 1:
        retorno = i

    del v[-1]

    return retorno


vetor = list(range(0, 10000000))

antes = time()
indice = busca_sequencial_sentinela(vetor, len(vetor) - 1)
print(indice)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))
