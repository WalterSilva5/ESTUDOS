from random import shuffle
from time import time

def insertion_sort(v):
    i = 1
    while i < len(v):
        temp = v[i]
        trocou = False
        j = i - 1
        while j >= 0 and temp < v[j]:
            v[j+1] = v[j]
            trocou = True
            j -= 1

        if trocou:
            v[j+1] = temp

        i += 1


vetor = list(range(0,100000))
shuffle(vetor)
#print(vetor)
antes = time()
insertion_sort(vetor)
depois = time()
total = (depois - antes) * 1000
#print(vetor)

print("Demorou {:.2f} ms para ordenar!".format(total))