import time

def busca_binaria(v, p, r, x):
    
    if p <= r:
        q = (p+r) // 2
        if x < v[q]:
            return busca_binaria(v, p, q-1, x)
        elif x > v[q]:
            return busca_binaria(v, q+1, r, x)
        else:
            return q
    
    return -1
            

vetor = list(range(0, 5))

antes = time.time()
posicao = busca_binaria(vetor, 0, len(vetor)-1, 2)
depois = time.time()
total = (depois-antes)*1000

if posicao >= 0:
    print("Encontrou o elemento na posição {}.".format(posicao))
else:
    print("Não encontrou o elemento.")

print("O tempo total foi {:.2f} ms".format(total))
