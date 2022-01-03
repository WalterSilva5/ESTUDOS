from time import time
from random import shuffle


def selection_sort(v):
    i = 0

    while i < len(v) - 1:
        menor = i
        j = i + 1
        # em busca do menor
        while j < len(v):
            if v[j] < v[menor]:
                menor = j
            j += 1

        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp

        i += 1


vetor = list(range(0, 10000))

shuffle(vetor)

antes = time()
selection_sort(vetor)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))