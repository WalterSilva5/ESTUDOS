import random
def bubbleSort(vetor):
    fim = len(vetor)

    while fim>0:
        elementoAtual =0
        while elementoAtual<fim-1:
            if vetor[elementoAtual] > vetor[elementoAtual+1]:
                temp = vetor[elementoAtual]
                vetor[elementoAtual] = vetor[elementoAtual+1]
                vetor[elementoAtual+1] = temp 
            elementoAtual+=1
        fim-=1

vetor = list(range(10)) 
random.shuffle(vetor)
print(vetor)
bubbleSort(vetor)
print(vetor)
