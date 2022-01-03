class No:
    def __init__(self, valor):
        self.valor = valor
        self.direita = None
        self.esquerda = None

    def __str__(self):
        return f'NO: {self.valor}'


class Arvore:
    def __init__(self):
        self.raiz = None
        self.quantidadeFolhas = 0

        if no.valor > perc.valor:
            if perc.direita == None:
                perc.direita = no
            else:

                self.__addNo(no, perc.direita)
        elif no.valor < perc.valor:
            if perc.esquerda == None:
                perc.esquerda = no
            else:
                self.__addNo(no, perc.esquerda)

        else:
            raise ("numero já existe")

    def add(self, valor):
        no = No(valor)
        if self.raiz == None:
            self.raiz = no
        else:
            self.__addNo(no, self.raiz)
        self.quantidadeFolhas += 1

    def __buscarNo(self, valor, percorredor, pai):
        perc = percorredor
        if perc == None:
            return None, pai
        if perc.valor == valor:
            return perc, pai
        else:
            if valor > perc.valor:
                return self.__buscarNo(valor, perc.direita, perc)
            else:
                return self.__buscarNo(valor, perc.esquerda, perc)

    def buscar(self, valor):
        if self.quantidadeFolhas == 0:
            return False
        busca, pai = self.__buscarNo(valor, self.raiz, None)
        if busca is None:
            return False
        return True

    def __imprimir(self, perc):
        if perc != None:
            print(perc)
            self.__imprimir(perc.esquerda)
            self.__imprimir(perc.direita)

    def imprimir(self):
        self.__imprimir(self.raiz)

    def __min(self, perc):
        pass

    def __max(self, perc):
        pass

    def __sucessor(self, perc):
        pass

    def __antecessor(self, perc):
        pass

    def remover(self, valor):
        pass


arvore = Arvore()
arvore.add(100)
arvore.add(200)
arvore.add(180)
arvore.add(70)
arvore.add(300)
arvore.add(60)
arvore.add(65)
arvore.add(50)
# print(arvore.buscar(70))
# print(arvore.quantidadeFolhas)
# arvore.imprimir()

# arvore.teste()

arvore.remover(70)
arvore.imprimir()
