import random
import time

def merge_sort(v, p, r):
    if p < r:
        q = (p+r) // 2 # descobrindo o meio do vetor
        merge_sort(v, p, q) # quebrar no sub-vetor 1
        merge_sort(v, q+1, r) # quebrar no sub-vetor 2
        intercalar(v, p, q, r) # intercalar os 2 sub-vetores


def intercalar(v, p, q, r):
    temp = v.copy()
    
    i = p
    j = q + 1
    k = p
    while k <= r:
        if i > q:
            #primeiro sub-vetor já terminou
            #copiar todos os elementos do segundo sub-vetor
            v[k] = temp[j]
            j += 1
        elif j > r:
            #segundo sub-vetor já terminou
            #copiar todos os elementos do segundo sub-vetor
            v[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            #se o elemento do primeiro sub-vetor for menor (ou igual)
            #copiar esse elemento menor (ou igual)
            v[k] = temp[i]
            i += 1
        else:
            #se o elemento do segundo sub-vetor for maior
            #copar esse elemento
            v[k] = temp[j]
            j += 1
            
        k += 1

vetor = list(range(0,100000))
#vetor = [3, 0, 2, 1, 4]

random.shuffle(vetor)
#print(vetor)
antes = time.time()
merge_sort(vetor, 0, len(vetor)-1)
depois = time.time()
total = (depois - antes) * 1000
print("O tempo total da ordenação foi: {:.2f} ms".format(total))
#print(vetor)

