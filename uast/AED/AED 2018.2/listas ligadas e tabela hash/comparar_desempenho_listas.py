from time import time
from listas_ligadas import Lista

lista = list(range(1000001))
lista2 = Lista(lista)
antes1 = time()
print(lista[1000000])
depois1 = time()

total1 = (depois1 - antes1) * 1000


antes2 = time()
print(lista2[1000000])
depois2 = time()

total2 = (depois2 - antes2) * 1000

print('tempo total lista built-in foi de {:.2f} ms'.format(total1))
print('tempo total lista ligada foi de {:.2f} ms'.format(total2))