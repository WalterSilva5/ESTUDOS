import time

def busca_sequencial(v, x):
    i = 0
    v.append(x)
    while v[i] != x:
        i += 1

    if i == len(v) - 1:
        return -1

    return i
        

vetor = list(range(0, 100000001))
#print("Vetor original: ")
#print(vetor)
antes = time.time()
posicao = busca_sequencial(vetor, 100000000)
#print("Vetor com sentinela: ")
#print(vetor)
depois = time.time()
total = (depois-antes)*1000

if posicao >= 0:
    print("Encontrou o elemento na posição {}.".format(posicao))
else:
    print("Não encontrou o elemento.")

print("O tempo total foi {:.2f} ms".format(total))