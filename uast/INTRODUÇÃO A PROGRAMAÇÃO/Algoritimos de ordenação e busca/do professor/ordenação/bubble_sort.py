from random import shuffle
from time import time

def bubble_sort(v):
    fim = len(v)
    while fim > 0:
        i = 0
        while i < fim - 1:
            if v[i] > v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
            i += 1
        fim -= 1

vetor = list(range(0,10000))
shuffle(vetor)
#print(vetor)
antes = time()
bubble_sort(vetor)
depois = time()
total = (depois-antes)*1000
#print(vetor)
print("Demorou {:.2f} ms para ordenar!".format(total))