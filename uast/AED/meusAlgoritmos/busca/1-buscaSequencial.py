import random 
vetor = list(range(10))
random.shuffle(vetor)
alvo = 5
pos = 0
print(list(range(10)))
print(vetor)
def buscaSeq(vetor, alvo, pos):
    if pos == len(vetor):
        return -1
    elif vetor[pos] == alvo:
        return pos 
    else:
        pos+=1
        return buscaSeq(vetor, alvo, pos)

print(buscaSeq(vetor, alvo, pos))
