#####################################################
# HEAP DE MÁXIMO                                    #
#   - Estrutura de dados Heap                       #
#   - Ordenação por Heap                            #
#   - Fila de prioridade máxima                     #
# Versão implementada com listas built-in do Python #
# Prof. Ygor Amaral - UFRPE/UAST                    #
#####################################################


class Heap:
    def __init__(self, heap=None):
        # __heap é um atributo privado
        if heap is None:
            self.__heap = []
        else:
            self.__heap = heap

    def __getitem__(self, i):
        return self.__heap[i]

    def __len__(self):
        return len(self.__heap)

    def __str__(self):
        return self.__heap.__str__()

    @property
    def heap(self):
        return self.__heap

    @heap.setter
    def heap(self, obj):
        self.__heap = list(obj)

    # onde está o pai de i?
    def pai(self, i):
        _pai = (i - 1) / 2  # se for negativo, não tem pai

        # se tiver pai, retornar o valor inteiro
        # caso contrário, retorne nulo
        return int(_pai) if _pai >= 0 else None  # por ter divisão, pai precisa ser convertido pra inteiro

    # onde está o filho da esquerda de i?
    def esquerda(self, i):
        _esquerda = (2 * i) + 1

        # se _esquerda for menor que a quantidade de elementos
        # significa que possui filho a esquerda
        return _esquerda if _esquerda < len(self) else None

    # onde está o filho da direita de i?
    def direita(self, i):
        _direita = (2 * i + 1) + 1

        # se _direita for menor que a quantidade de elementos
        # significa que possui filho a direita
        return _direita if _direita < len(self) else None

    # manter a propriedade de heap de máximo em todo o arranjo
    def construir_heap(self):
        i = (len(self) // 2) - 1  # índice do último nó que é pai
        while i >= 0:
            self.heapify(i)
            i -= 1

    # manter a propriedade de heap de máximo no nó i
    def heapify(self, i):
        e = self.esquerda(i)
        d = self.direita(i)

        # se tiver filho da esquerda e ele for maior que o nó i (que é o pai)
        # então o filho da esquerda poderá trocar de posição com o pai
        if e is not None and self[e] > self[i]:
            maior = e
        else:
            maior = i

        # se tiver filho da direita e ele for maior que o nó maior (seja o irmão da esquerda ou o pai)
        # então o filho da direita poderá trocar de posição com o maior anterior
        if d is not None and self[d] > self[maior]:
            maior = d

        # se o filho da esquerda ou direita for maior, então troca de posição com i
        if maior != i:
            # trocar 'i' com 'maior'
            self.__heap[i], self.__heap[maior] = self.__heap[maior], self.__heap[i]

            # verificar a propriedade de heap de máximo
            # justamente onde o antigo pai que violava a propriedade de heap de máximo foi parar
            self.heapify(maior)

    def extrair_máximo(self):
        if len(self) > 0:
            # na raiz sempre está o maior elemento do heap atual
            máximo = self[0]

            # pega o último elemento do heap e coloca na raiz (sobrescreve)
            self.__heap[0] = self.__heap[-1]

            # apaga o último elemento do heap (ele agora está na raiz)
            del self.__heap[-1]  # heap vai diminuindo de tamanho

            # usar o heapify para colocar o elemento da raiz em sua nova posição correta do heap
            self.heapify(0)

            return máximo
        else:
            return None

    # heapsort
    def sort(self):
        self.construir_heap()

        ordenado = []  # arranjo auxiliar, irá inserir os elementos já na sua posição ordenada

        i = len(self) - 1  # última posição do heap
        while i >= 0:
            # pega o máximo do heap e insere na posição correta do arranjo ordenado
            ordenado.insert(0, self.extrair_máximo())  # ordem crescente
            # ordenado.append(self.extrair_máximo()) # ordem decrescente

            # nova última posição do heap
            i -= 1

        self.__heap = ordenado

    # método para fila de prioridade
    # aumentar a prioridade (chave) do nó i
    def aumentar_chave(self, i, chave):
        # só irá trabalhar se a chave for maior do que a chave existente no nó i
        if chave > self[i]:
            self.__heap[i] = chave  # atualizando a chave

            # enquanto não for o nó raiz, verificar se o pai de i é menor do que i
            # caso seja, então viola a propriedade de máximo, precisará ser trocado
            while i > 0 and self[self.pai(i)] < self[i]:
                self.__heap[i], self.__heap[self.pai(i)] = self.__heap[self.pai(i)], self.__heap[i]

                # a próxima verificação será onde i foi parar (no lugar do seu antigo pai)
                i = self.pai(i)

    # método para fila de prioridade
    # inserir um novo nó com uma determinada prioridade (chave)
    def inserir(self, chave):
        # adicionando o novo nó no final do arranjo, inicialmente com uma prioridade arbitrariamente menor
        self.__heap.append(chave - 1)

        # aumentar a prioridade (chave) do novo nó adicionado
        # esse método colocará esse novo nó no seu devido lugar dentro do heap de máximo
        self.aumentar_chave(len(self) - 1, chave)  # mantendo a propriedade de heap de máximo
