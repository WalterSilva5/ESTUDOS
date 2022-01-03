import time
"""
codigos no github se precisar conferir os commits
https://github.com/WalterSilva5/uast/tree/master/INTRODU%C3%87%C3%83O%20A%20PROGRAMA%C3%87%C3%83O/Projeto%202%20va
"""


def inicio():
    while True:
        tam = int(input("TAMANHO DO VETOR: "))
        if tam <= 4:
            print("O TAMANHO DO VETOR DEVE SER MAIOR QUE QUATRO!")
            continue
        else:
            lista = list(range(tam))
            break
    opções = ["BUSCA SEQUENCIAL", "BUSCA SEQUENCIAL COM SENTINELA", "BUSCA BINARIA"]
    while True:
        alg_a = int(input("""
        TIPOS DE ALGORITMOS DE BUSCA
1 - BUSCA SEQUENCIAL
2 - BUSCA SEQUENCIAL COM SENTINELA
3 - BUSCA BINARIA

ESCOLHA 2 OPÇÕES PARA COMPARAR
A: """))
        alg_b = int(input("B: "))
        if alg_a < 0 or alg_a > 6:
            print("ESCOLHA APENAS NUMEROS DE 1 A 3")
            continue
        elif alg_b < 0 or alg_b > 6:
            print("ESCOLHA APENAS NUMEROS DE 1 A 3")
            continue
        elif alg_a == alg_b:
            print("VOCÊ DEVE ESCOLHER DOIS ALGORITMOS DIFERENTES!")
            continue
        else:
            break
    while True:
        try:
            elemento = int(input("Qual elemento deseja buscar?"))
        except Exception:
            print("DIGITE APENAS NUMEROS INTEIROS!")
            continue
        else:
            break
    # testa a opção escolhida
    resultado_a, encontrado_a = testa_algoritmo(alg_a, lista, elemento)
    resultado_b, encontrado_b = testa_algoritmo(alg_b, lista, elemento)

    if encontrado_a:
        print("O ALGORITMO - {} - DEMOROU {:.5f} MILISSEGUNDOS ENCONTRAR O ELEMENTO".format(opções[alg_a - 1], resultado_a))
    else:
        print("O ALGORITMO - {} - DEMOROU {:.5f} MILISSEGUNDOS PARA PERCORRER O VETOR\nPOREM O ELEMENTO NÃO FOI ENCONTRADO".format(
            opções[alg_a - 1], resultado_a))
    if encontrado_b:
        print("O ALGORITMO - {} - DEMOROU {:.5f} MILISSEGUNDOS ENCONTRAR O ELEMENTO".format(opções[alg_b - 1], resultado_b))
    else:
        print("O ALGORITMO - {} - DEMOROU {:.5f} MILISSEGUNDOS PARA PERCORRER O VETOR\nPOREM O ELEMENTO NÃO FOI ENCONTRADO".format(
            opções[alg_b - 1], resultado_b))

    if resultado_a < resultado_b:
        print("\nO ALGORITMO - {} - FOI MAIS EFICIENTE E DEMOROU {:.5f} MILISSEGUNDOS A MENOS QUE O - {} -.".format(
            opções[alg_a - 1], resultado_b - resultado_a, opções[alg_b - 1]))
    elif resultado_b < resultado_a:
        print("\nO ALGORITMO - {} - FOI MAIS EFICIENTE E DEMOROU {:.5f} MILISSEGUNDOS A MENOS QUE O - {} -.".format(
            opções[alg_b - 1], resultado_a - resultado_b, opções[alg_a - 1]))
    else:
        print(
            "\nOS ALGORITMOS - {} - E - {} - TIVERAM A MESMA EFICIENCIA E DEMORARAM {:.5f} MILISSEGUNDOS  PARA ORDENAR.".format(
                opções[alg_a - 1], opções[alg_b - 1], resultado_a))


# funcao que testa as opções escolhidas
def testa_algoritmo(opcao, lista, elemento):
    if opcao == 1:
        copia = lista.copy()
        antes = time.time()
        posicao = busca_sequencial(copia, elemento)
        encontrado = False
        if posicao >=0:
            encontrado = True
        depois = time.time()
        return (depois - antes) * 1000, encontrado
    if opcao == 2:
        copia = lista.copy()
        antes = time.time()
        posicao = busca_sequencial_sentinela(copia, elemento)
        encontrado = False
        if posicao >=0:
            encontrado = True
        depois = time.time()
        return (depois - antes) * 1000, encontrado
    if opcao == 3:
        copia = lista.copy()
        antes = time.time()
        posicao = busca_binaria(copia, 0, len(copia)-1, elemento)
        encontrado = False
        if posicao >=0:
            encontrado = True
        depois = time.time()
        return (depois - antes) * 1000, encontrado

def busca_sequencial_sentinela(vetor, elemento):
    posicao = 0
    vetor.append(elemento)
    while vetor[posicao] != elemento:
        posicao += 1
    if posicao == len(vetor) - 1:
        return -1
    return posicao

def busca_sequencial(vetor, elemento):
    posicao = 0
    while posicao < len(vetor):
        if vetor[posicao] == elemento:
            return posicao
        posicao += 1
    return -1

def busca_binaria(vetor, pos_inicial, pos_final, x):
    if pos_inicial <= pos_final:
        meio = (pos_inicial + pos_final) // 2
        if x < vetor[meio]:
            return busca_binaria(vetor, pos_inicial, meio - 1, x)
        elif x > vetor[meio]:
            return busca_binaria(vetor, meio + 1, pos_final, x)
        else:
            return meio
    return -1

inicio()