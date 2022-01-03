class No:
    def __init__(self, valor):
        self.pai = None
        self.esquerda = None
        self.direita = None
        self.valor = valor

        def __str__(self):
            return self.valor

        def __repr__(self):
            return self.__str__()
            
class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None
        self.numeroDeFolhas = 0

    def add(self, valor):
        no = No(valor)
        atual = self.__raiz
        if atual is None:
            self.__raiz = no
        else:
            self.addRec(self.__raiz, no, atual.pai)# começa pela raiz
        self.numeroDeFolhas+=1

    def addRec(self, atual, no, pai):
        no.pai = pai
        if no.valor > atual.valor:
            if atual.direita is None:
                atual.direita = no
            else:
                self.addRec(atual.direita, no, atual) 
        elif no.valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = no
            else:
                self.addRec(atual.esquerda, no, atual)
        else:
            raise Exception("valor ja esta na lista")

    def buscar(self, valor):
        atual = self.__raiz

        if atual.valor == valor:
            return atual
        else:
            no = self.buscarNoRec(atual, valor)
            if no is None:
                raise Exception("valor não esta na arvore")
            else:
                return no

    def buscarNoRec(self, atual, valor):
        if atual is None:
            return atual
        elif atual.valor > valor:
            return self.buscarNoRec(atual.esquerda, valor)
        elif atual.valor < valor:
            return self.buscarNoRec(atual.direita, valor)
        else:
            return atual



    def minimo(self, atual= None):
        if self.__raiz is None:
            raise Exception("Arvore vazia")
        if atual is None:
            atual = self.__raiz
        if atual.esquerda is not None:
            return self.minimo(atual.esquerda)
        else:
            return atual.valor
    
    def maximo(self, atual= None):
        if self.__raiz is None:
            raise Exception("Arvore vazia")
        if atual is None:
            atual = self.__raiz
        if atual.direita is not None:
            return self.maximo(atual.direita)
        else:
            return atual


    def imprimirRec(self, atual):
        if atual != None:
            print(atual.valor)
            self.imprimirRec(atual.esquerda)
            self.imprimirRec(atual.direita)

    def imprimir(self):
        self.imprimirRec(self.__raiz)


    def sucessor(self, valor):
        atual = self.buscar(valor)

        if atual is None:
            return atual

        if atual.direita is not None:
            return self.minimo(atual.direita)

        if atual.pai is not None and atual == atual.pai.esquerda:
            return atual.pai
        else:
            sucessor = self.buscarSucessorRec(atual.pai)
            return sucessor

    def buscarSucessorRec(self, atual):
        if atual.pai is not None and atual == atual.pai.direita:
            return self.buscarSucessorRec(atual.pai)
        if atual.pai is None:
            return atual
        return atual.pai

    def antecessor(self, valor):
        atual = self.buscar(valor)

        if atual is None:
            return atual

        if atual.esquerda is not None:
            return self.minimo(atual.esquerda)

        if atual.pai is not None and atual == atual.pai.direita:
            return atual.pai
        else:
            sucessor = self.buscarSucessorRec(atual.pai)
            return sucessor
    
    def recortar(self, sera_removido, sera_recortado):
        if sera_removido.pai is None:
            self.raiz = sera_recortado
        elif sera_removido == sera_removido.pai.esquerda:
            sera_removido.pai.esquerda = sera_recortado
        else:
            sera_removido.pai.direita = sera_recortado
            
        if sera_recortado is not None:
            sera_recortado.pai = ser_removido.pai
        
    def remover(self, valor):
        alvo = self.buscar(valor)
        
        if alvo.esquerda is None:
            self.recortar(alvo, alvo.direita)
        elif alvo.direita is None:
            self.recortar(alvo, alvo.esquerda)
        else:
            sucessor = self.sucessor(alvo.valor)

##########################################
a = ArvoreBuscaBinaria()

a.add(6)
a.add(3)
a.add(4)
a.add(8)
a.add(7)
a.add(10)


print(a.sucessor(4).valor)