from time import time


def busca_binaria(v, x):
    p = 0
    r = len(v) - 1

    while p <= r:
        q = (p + r) // 2
        if x < v[q]:
            r = q - 1
        elif x > v[q]:
            p = q + 1
        else:
            return q

    return -1


vetor = list(range(0, 10000000))

antes = time()
indice = busca_binaria(vetor, len(vetor) - 1)
print(indice)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))
