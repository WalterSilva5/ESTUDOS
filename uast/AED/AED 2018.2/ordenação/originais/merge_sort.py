from time import time
from random import shuffle


def merge_sort(v, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(v, p, q)
        merge_sort(v, q + 1, r)
        intercalar(v, p, q, r)


def intercalar(v, p, q, r):
    temp = v.copy()

    i = p  # índice do primeiro sub-vetor
    j = q + 1  # índice do segundo sub-vetor
    k = p  # índice do vetor
    while k <= r:
        if i > q:
            # primeiro sub-vetor já terminou
            # copiar todos os elementos do segundo sub-vetor
            v[k] = temp[j]
            j += 1
        elif j > r:
            # segundo sub-vetor já terminou
            # copiar todos os elementos do segundo sub-vetor
            v[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            # se o elemento do primeiro sub-vetor for menor (ou igual)
            # copiar esse elemento menor (ou igual)
            v[k] = temp[i]
            i += 1
        else:
            # se o elemento do segundo sub-vetor for maior
            # copar esse elemento
            v[k] = temp[j]
            j += 1

        k += 1


vetor = list(range(0, 100000))

shuffle(vetor)

antes = time()
merge_sort(vetor, 0, len(vetor) - 1)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))
