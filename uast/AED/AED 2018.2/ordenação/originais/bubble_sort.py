from time import time
from random import shuffle


def bubble_sort(v):
    fim = len(v) - 1

    while fim > 0:
        i = 0
        while i < fim:
            if v[i] > v[i + 1]:
                temp = v[i + 1]
                v[i + 1] = v[i]
                v[i] = temp
            i += 1
        fim -= 1


vetor = list(range(0, 10000))

shuffle(vetor)

antes = time()
bubble_sort(vetor)
depois = time()
total = (depois - antes) * 1000
print("Tempo total: {:.2f} ms".format(total))
