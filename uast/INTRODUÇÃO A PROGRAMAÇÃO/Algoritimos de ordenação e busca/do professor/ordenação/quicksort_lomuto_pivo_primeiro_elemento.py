import time


def quicksort(v, p, r):
    if p < r:
        q = particionar(v, p, r) # escolher e colocar o pivô na posição correta
        quicksort(v, p, q-1) #pivotar a esquerda
        quicksort(v, q+1, r) #pivotar a direita
        
def particionar(v, p, r):
    x = v[p] #escolhendo o pivô
    i = p
    j = p + 1
    while j <= r:
        if v[j] < x:
            i += 1
            trocar(v, i, j) #puxando o elemento menor que o pivô
        j += 1
    
    trocar(v, p, i)
    
    return i

def trocar(v, n, m):
    temp = v[n]
    v[n] = v[m]
    v[m] = temp

#vetor = list(range(0,100000))
#random.shuffle(vetor)
vetor = [9,3,4,2,5,8,7,1]
print(vetor)
antes = time.time()
quicksort(vetor, 0, len(vetor)-1)
depois = time.time()
total = (depois - antes) * 1000
print("O tempo total da ordenação foi: {:.2f} ms".format(total))
print(vetor)

