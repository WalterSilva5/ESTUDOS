from time import time
from random import shuffle
from heap import Heap

#gerada = list(range(100000))
#shuffle(gerada)

gerada = [8, 2, 7, 6, 4]
teste = Heap(gerada)
print(teste)

for i in range(len(teste)):
    valor_nó = teste[i]
    índice_pai = teste.pai(i)
    if índice_pai is not None:
        valor_pai = teste[índice_pai]
    else:
        valor_pai = None

    print('Nó: {}'.format(valor_nó))
    print('\tÍndice Nó: {} / Índice pai: {} / Nó: {} / Valor pai: {}'
          .format(i, índice_pai, valor_nó, valor_pai))
    print('\tFilho da Esquerda: {} / Filho da Direita: {}'
          .format(teste.esquerda(i), teste.direita(i)))

#print(len(teste))


# antes = time()
# teste.sort()
# depois = time()
# total = (depois - antes) * 1000
# print('O tempo total foi: {:.2f} ms'.format(total))
#print(teste)

#print(teste)
#teste.construir_heap()
#print(teste)
#teste.aumentar_chave(9, 11)
#print(teste)
#teste.inserir(15)

#print(teste.extrair_máximo())
#print(teste.extrair_máximo())
#print(teste)
#print(teste.extrair_máximo())
