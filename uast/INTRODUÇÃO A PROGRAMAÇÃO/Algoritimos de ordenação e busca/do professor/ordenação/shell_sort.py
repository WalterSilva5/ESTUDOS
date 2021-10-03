from random import shuffle
from time import time


def shell_sort(v):

    h = len(v) // 2 # distância inicial
    while h > 0:
        i = h
        while i < len(v):
            temp = v[i]
            trocou = False
            j = i - h
            while j >= 0 and temp < v[j]:
                v[j+h] = v[j]
                trocou = True
                j -= h

            if trocou:
                v[j+h] = temp

            i += 1

        h = h // 2


vetor = list(range(0,100000))
shuffle(vetor)
#print(vetor)
antes = time()
shell_sort(vetor)
depois = time()
total = (depois - antes) * 1000
#print(vetor)

print("Demorou {:.2f} ms para ordenar!".format(total))