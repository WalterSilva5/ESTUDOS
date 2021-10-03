from random import shuffle
from time import time

def selection_sort(v):
    i = 0
    while i < len(v) - 1:
        menor = i # inicializando o menor
        j = i + 1 # com quem a gente vai comparar o menor
        # descobrir de fato, quem é o menor
        while j < len(v):
            if v[j] < v[menor]:
                menor = j
            j += 1

        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp

        i += 1


vetor = list(range(0,100000))
shuffle(vetor)
#print(vetor)
antes = time()
selection_sort(vetor)
depois = time()
total = (depois-antes)*1000
#print(vetor)
print("Demorou {:.2f} ms para ordenar!".format(total))