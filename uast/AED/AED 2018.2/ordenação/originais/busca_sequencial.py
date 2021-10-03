from time import time


def busca_sequencial(v, x):
    i = 0
    while i < len(v):
        if v[i] == x:
            return i
        i += 1

    return -1


vetor = list(range(0, 10000000))

antes = time()
indice = busca_sequencial(vetor, len(vetor)-1)
print(indice)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))