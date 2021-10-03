import collections

class Lista(object):
    def __init__(self, valores=None):
        self.inicio = None
        self.fim = None
        self._meio = None
        self.__tam = 0

        if valores is not None:
            self.extend(valores)

    class No:
        def __init__(self, valor):
            self.valor = valor
            self.anterior = None
            self.proximo = None

    def adicionar(self, valor):
        no = self.No(valor)
        if self.fim is None:
            self.inicio = no
            self.inicio.anterior = no
            self.inicio.proximo = no
            self.fim = no
            self._meio = no
        else:
            no.proximo = self.inicio
            no.anterior = self.fim
            self.fim.proximo = no
            self.fim = no
        self.moveMeioParaFrente()

    def moveMeioParaFrente(self):
        """usado em qualquer metodo que adiciona um no a lista
        verifica se o numero de alterações na lista é par 
        e se for move o meio da lista para frente"""
        self.__tam += 1
        if (self.__tam % 2 == 0):
            self._meio = self._meio.proximo

    def moveMeioParaTras(self):
        """usado ao remover um item da lista
        verifica se o numero de alterações na lista é par 
        e se for move o meio da lista para tras"""
        self.__tam -= 1
        if (self.__tam % 2 == 0):
            self._meio = self._meio.anterior

    def listar(self):
        if self.__tam == 0:
            return "[]"
        lista = "["
        atual = self.inicio
        for c in range(self.__tam):
            lista += "{}, ".format(atual.valor)
            atual = atual.proximo

        lista = lista[:-2] + "]"
        return lista

    def editar(self, posicao, valor):
        """muda o valor de um elemento"""
        no = self.buscarPorPosicao(posicao)
        no.valor = valor

    def buscarPorPosicao(self, posicao):
        """retorna um no"""
        if self.__tam == 0:
            raise AttributeError("Lista não tem elementos")
        if posicao < 0 or posicao > self.__tam:
            raise IndexError("lista não tem essa posicao")
        atual = self._meio
        cont = self.__tam // 2
        if posicao > self.__tam // 2:
            while cont < posicao:
                atual = atual.proximo
                cont += 1
        else:
            while cont > posicao:
                atual = atual.anterior
                cont -= 1
        return atual

    def removerPorPosicao(self, posicao):
        """remove um elemento da lista em uma determinada posicao"""
        no = self.buscarPorPosicao(posicao)
        if no.proximo == no:
            # caso so tenha um elemento e esteja removendo o unico elemento
            self.fim = None
        no.anterior.proximo = no.proximo
        self.moveMeioParaTras()
        return no.valor

    def buscarPorValor(self, valor):
        """retorna o indicice da primeira ocorrencia do valor na lista,
        caso o valor exista na lista"""
        atual = self.inicio
        cont = 0
        while atual.valor != valor and cont < self.__tam - 1:
            print("atual: {}".format(atual.valor))
            atual = atual.proximo
            cont += 1

        if atual == self.fim and atual.valor != valor:
            raise ValueError("não encontrado")
        return cont

    def removerPorValor(self, valor):
        """encontra a posicao que o valor esta na lista e o remove"""
        posicao = self.buscarPorValor(valor)
        self.removerPorPosicao(posicao)

    def inserir(self, posicao, valor):
        # antigo que estava na posicao que queremos inserir
        antigo = self.buscarPorPosicao(posicao)
        if posicao == self.__tam:
            self.adicionar(valor)
        else:
            no = self.No(valor)
            no.anterior = antigo.anterior
            no.proximo = antigo
            antigo.anterior = no
            no.anterior.proximo = no
            self.moveMeioParaFrente()

    @property
    def meio(self):
        return self._meio.valor

    def numeroDeOcorrencias(self, valor):
        """retorna o numero de ocorrencias de um valor na lista"""
        cont = 0
        ocorrencias = 0
        atual = self.inicio
        while cont < self.__tam:
            if atual.valor == valor:
                ocorrencias += 1
            cont += 1
            atual = atual.proximo

    def inverter(self):
        novaLista = self.copy()
        self.clear()
        cont = len(novaLista)
        atual = novaLista.fim
        while cont > 0:
            self.adicionar(atual.valor)
            atual = atual.anterior
            cont -= 1

    ############################
    ### metodos sobrescritos ###
    ############################
    def __getitem__(self, posicao):
        return self.buscarPorPosicao(posicao).valor

    def __str__(self):
        return self.listar()

    def __len__(self):
        return self.__tam

    def __delitem__(self, posicao):
        return self.removerPorPosicao(posicao)

    def __setitem__(self, key, value):
        return self.editar(key, value)

    def append(self, valor):
        return self.adicionar(valor)

    def insert(self, posicao, valor):
        return self.inserir(posicao, valor)

    def clear(self):
        """limpa a lista"""
        self.inicio, self._meio, self.fim = None, None, None
        self.__tam = 0

    def index(self, valor):
        return self.buscarPorValor(valor)

    def count(self, valor):
        return self.numeroDeOcorrrencias(valor)

    def copy(self):
        novaLista = Lista()
        atual = self.inicio
        for elemento in range(self.__tam):
            novaLista.adicionar(atual.valor)
            atual = atual.proximo
        return novaLista

    def extend(self, iteravel):
        if isinstance(iteravel, collections.Iterable):
            for elemento in iteravel:
                self.adicionar(elemento)
        else:
            raise Exception("argumento não é iteravel")

    def pop(self, posicao=None):
        if posicao is None:
            return self.removerPorPosicao(self.__tam - 1)
        else:
            return self.removerPorPosicao(posicao)

    def reverse(self):
        return self.inverter()