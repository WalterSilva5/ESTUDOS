import random
import time
"""
codigos no github se precisar conferir os commits
https://github.com/WalterSilva5/uast/tree/master/INTRODU%C3%87%C3%83O%20A%20PROGRAMA%C3%87%C3%83O/Projeto%202%20va
"""
def inicio():
    opções = ["BUBBLE SORT","SELECTION SORT","INSERTION SORT","SHELL SORT","MERGE SORT","QUICK SORT"]
    while True:
        tam = int(input("TAMANHO DO VETOR: "))
        if tam <=4:
            print("O TAMANHO DO VETOR DEVE SER MAIOR QUE QUATRO!")
            continue
        lista = list(range(tam))
        random.shuffle(lista)
        alg_a = int(input("""
        TIPOS DE ALGORITMOS DE ORDENAÇÃO
1 - BUBBLE SORT
2 - SELECTION SORT
3 - INSERTION SORT
4 - SHELL SORT
5 - MERGE SORT
6 - QUICK SORT
ESCOLHA 2 OPÇÕES PARA COMPARAR
A: """))
        alg_b = int(input("B: "))
        if alg_a <0 or alg_a>6:
            print("ESCOLHA APENAS NUMEROS DE 1 A 6")
            continue
        elif alg_b <0 or alg_b>6:
            print("ESCOLHA APENAS NUMEROS DE 1 A 6")
            continue
        elif alg_a == alg_b:
            print("VOCÊ DEVE ESCOLHER DOIS ALGORITMOS DIFERENTES!")
            continue
        else:
            break
    #testa a opção escolhida
    resultado_a = testa_algoritmo(alg_a, lista)
    resultado_b = testa_algoritmo(alg_b, lista)

    print("O ALGORITMO - {} - DEMOROU {:.2f} MILISSEGUNDOS PARA ORDENAR O VETOR".format(opções[alg_a-1], resultado_a))
    print("O ALGORITMO - {} - DEMOROU {:.2f} MILISSEGUNDOS PARA ORDENAR O VETOR".format(opções[alg_b-1], resultado_b))
    
    if resultado_a < resultado_b:
        print("\nO ALGORITMO - {} - FOI MAIS EFICIENTE E DEMOROU {:.2f} MILISSEGUNDOS A MENOS QUE O - {} -.".format(
            opções[alg_a-1], resultado_b-resultado_a, opções[alg_b-1]))
    elif resultado_b < resultado_a:
        print("\nO ALGORITMO - {} - FOI MAIS EFICIENTE E DEMOROU {:.2f} MILISSEGUNDOS A MENOS QUE O - {} -.".format(
            opções[alg_b-1], resultado_a-resultado_b, opções[alg_a-1]))
    else:
        print("\nOS ALGORITMOS - {} - E - {} - TIVERAM A MESMA EFICIENCIA E DEMORARAM {:.2f} MILISSEGUNDOS  PARA ORDENAR.".format(
            opções[alg_a - 1], opções[alg_b - 1], resultado_a))

#funcao que testa as opções escolhidas
def testa_algoritmo(opcao, lista):
    if opcao == 1:
        copia = lista.copy()
        antes = time.time()
        bubble_sort(copia)
        depois = time.time()
        return (depois-antes)*1000
    elif opcao == 2:
        copia = lista.copy()
        antes = time.time()
        selection_sort(copia)
        depois = time.time()
        return (depois-antes)*1000
    elif opcao == 3:
        copia = lista.copy()
        antes = time.time()
        insertion_sort(copia)
        depois = time.time()
        return (depois-antes)*1000
    elif opcao == 3:
        copia = lista.copy()
        antes = time.time()
        shell_sort(copia)
        depois = time.time()
        return (depois-antes)*1000
    elif opcao == 4:
        copia = lista.copy()
        antes = time.time()
        shell_sort(copia)
        depois = time.time()
        return (depois-antes)*1000
    elif opcao == 5:
        copia = lista.copy()
        antes = time.time()
        merge_sort(copia, 0, len(copia)-1)
        depois = time.time()
        return (depois-antes)*1000
    elif opcao == 6:
        copia = lista.copy()
        antes = time.time()
        quick_sort(copia, 0, len(copia)-1)
        depois = time.time()
        return (depois-antes)*1000

####bubble sort
def bubble_sort(vetor):
    fim = len(vetor)
    while fim > 0:
        contador = 0
        while contador < fim - 1:
            if vetor[contador] > vetor[contador+1]:
                temp = vetor[contador]
                vetor[contador] = vetor[contador+1]
                vetor[contador+1] = temp
            contador+= 1
        fim -= 1

####selection sort
def selection_sort(vetor):
    contador_1 = 0
    while contador_1 < len(vetor) - 1:
        menor = contador_1
        contador_2 = contador_1 + 1
        while contador_2 < len(vetor):
            if vetor[contador_2] < vetor[menor]:
                menor = contador_2
            contador_2 += 1
        if menor != contador_1:
            temp = vetor[contador_1]
            vetor[contador_1] = vetor[menor]
            vetor[menor] = temp
        contador_1 += 1

####insertion sort
def insertion_sort(vetor):
    contador = 1
    while contador < len(vetor):
        temp = vetor[contador]
        trocou = False
        contador_2 = contador - 1
        while contador_2 >= 0 and temp < vetor[contador_2]:
            vetor[contador_2+1] = vetor[contador_2]
            trocou = True
            contador_2 -= 1
        if trocou:
            vetor[contador_2+1] = temp
        contador += 1

####shell sort
def shell_sort(vetor):
    distancia = len(vetor) // 2
    while distancia > 0:
        contador = distancia
        while contador < len(vetor):
            temp = vetor[contador]
            trocou = False
            contador_2 = contador - distancia
            while contador_2 >= 0 and temp < vetor[contador_2]:
                vetor[contador_2+distancia] = vetor[contador_2]
                trocou = True
                contador_2 -= distancia
            if trocou:
                vetor[contador_2+distancia] = temp
            contador += 1
        distancia = distancia // 2

####merge sort
def merge_sort(vetor, pos_inicial, pos_final):
    if pos_inicial < pos_final:
        meio = (pos_inicial+pos_final) // 2 # descobrindo o meio do vetor
        merge_sort(vetor, pos_inicial, meio) # quebrar no sub-vetor 1
        merge_sort(vetor, meio+1, pos_final) # quebrar no sub-vetor 2
        intercalar(vetor, pos_inicial, meio, pos_final) # intercalar os 2 sub-vetores

def intercalar(vetor, pos_inicial, meio, pos_final):
    copia = vetor.copy()
    contador_1 = pos_inicial#percorre o primeiro subvetor
    contador_2 = meio + 1#percorre o segundo subvetor
    k = pos_inicial#percorre todo o vetor
    while k <= pos_final:
        if contador_1 > meio:
            vetor[k] = copia[contador_2]
            contador_2 += 1
        elif contador_2 > pos_final:
            vetor[k] = copia[contador_1]
            contador_1 += 1
        elif copia[contador_1] <= copia[contador_2]:
            vetor[k] = copia[contador_1]
            contador_1 += 1
        else:
            vetor[k] = copia[contador_2]
            contador_2 += 1
        k += 1
####quick_sort
import time


def quick_sort(vetor, pos_inicial, pos_final):
    if pos_inicial < pos_final:
        pivo = particionar(vetor, pos_inicial, pos_final)
        quick_sort(vetor, pos_inicial, pivo - 1)
        quick_sort(vetor, pivo + 1, pos_final)


def particionar(vetor, pos_inicial, pos_final):
    pivo = vetor[pos_inicial]
    contador_1 = pos_inicial
    contador_2 = pos_inicial + 1
    while contador_2 <= pos_final:
        if vetor[contador_2] < pivo:
            contador_1 += 1
            trocar(vetor, contador_1, contador_2)
        contador_2 += 1
    trocar(vetor, pos_inicial, contador_1)
    return contador_1


def trocar(vetor, a, b):
    #coloquei o nome das variaveis com letras diferentes da execução da função pois ela pode ser chamada em duas ocasiões!
    temp = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = temp


inicio()