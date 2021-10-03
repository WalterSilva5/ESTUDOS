from time import time
from random import shuffle


def insertion_sort(v):
    i = 1
    while i < len(v):
        troca = False
        temp = v[i]

        j = i - 1
        while j >= 0 and v[j] > temp:
            v[j + 1] = v[j]
            troca = True
            j -= 1

        if troca:
            v[j + 1] = temp

        i += 1


vetor = list(range(0, 10000))

shuffle(vetor)

antes = time()
insertion_sort(vetor)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))
