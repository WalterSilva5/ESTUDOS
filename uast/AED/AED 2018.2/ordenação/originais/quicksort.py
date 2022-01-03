from time import time
from random import shuffle


def quicksort(v, p, r):
    if p < r:
        q = particionar(v, p, r)
        quicksort(v, p, q - 1)  # pivotar a esquerda
        quicksort(v, q + 1, r)  # pivotar a direita


def particionar(v, p, r):
    x = v[p]  # escolhendo o pivô
    i = p
    j = p + 1
    while j <= r:
        if v[j] < x:
            i += 1
            trocar(v, i, j)  # puxando o elemento menor que o pivô
        j += 1

    trocar(v, p, i)

    return i


def trocar(v, n, m):
    temp = v[n]
    v[n] = v[m]
    v[m] = temp


vetor = list(range(0, 100000))

shuffle(vetor)

antes = time()
quicksort(vetor, 0, len(vetor) - 1)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))
