from time import time
from listas_ligadas import Lista

lista1 = list(range(1000001))

antes1 = time()
print(lista1[1000000])
#print(lista1[0])
depois1 = time()
total1 = (depois1 - antes1) * 1000

lista2 = Lista(lista1)
antes2 = time()
print(lista2[1000000])
#print(lista2[0])
depois2 = time()
total2 = (depois2 - antes2) * 1000

print('Lista built-in do Python demorou: {:.2f} ms'.format(total1))
print('Lista liga da gente demorou: {:.2f} ms'.format(total2))