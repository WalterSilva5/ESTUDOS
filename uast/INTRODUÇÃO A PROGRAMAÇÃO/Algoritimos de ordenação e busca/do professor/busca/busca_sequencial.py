import time

def busca_sequencial(v, x):
    i = 0
    while i < len(v):
        if v[i] == x:
            return i
        i += 1
    
    return -1
        

vetor = list(range(0, 100000001))
#print(vetor)
antes = time.time()
posicao = busca_sequencial(vetor, 100000000)
depois = time.time()
total = (depois-antes)*1000

if posicao >= 0:
    print("Encontrou o elemento na posição {}.".format(posicao))
else:
    print("Não encontrou o elemento.")

print("O tempo total foi {:.2f} ms".format(total))