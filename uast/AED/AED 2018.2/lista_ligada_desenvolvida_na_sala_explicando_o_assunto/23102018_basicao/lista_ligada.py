class Lista:
    def __init__(self):
        # atributos internos
        self.__primeiro = None
        self.__último = None
        self.__tamanho = 0

    def __len__(self):
        return self.__tamanho

    class Nó:
        def __init__(self, conteúdo):
            self.conteúdo = conteúdo
            self.próximo = None

    def __getitem__(self, índice):

        if isinstance(índice, slice):
            print('está tentando fazer um fatiamento/slice')
            _lista = Lista()

            start = 0 if índice.start is None else índice.start
            stop = len(self) if índice.stop is None else índice.stop
            step = 1 if índice.step is None else índice.step

            i = start
            while i < stop:
                _lista.inserir(len(_lista), self[i])
                i += step

            return _lista

        else:
            if índice < 0:
                índice += len(self)

            atual = self.__primeiro

            i = 0
            while atual is not None:
                if i == índice:
                    return atual.conteúdo

                atual = atual.próximo
                i += 1

            raise IndexError('o índice ultrapassou o limite da lista')

    def __delitem__(self, índice):
        anterior = None
        atual = self.__primeiro

        i = 0
        while atual is not None:
            if i == índice:
                if anterior is None: # apagando o primeiro elemento
                    self.__primeiro = atual.próximo
                else:
                    anterior.próximo = atual.próximo

                if índice == len(self) - 1:
                    self.__último = anterior

                atual.próximo = None

                self.__tamanho -= 1
                return

            anterior = atual
            atual = atual.próximo
            i += 1

    def __str__(self):
        retorno = '>'
        for i in range(len(self)):
            retorno += self[i].__repr__()

            if i < len(self) - 1:
                retorno += ', '

        retorno += '<'

        return retorno


    def inserir(self, índice, conteúdo):
        novo = self.Nó(conteúdo)

        # se é uma lista vazia
        if self.__primeiro is None:
            self.__primeiro = novo
            self.__último = novo
        elif índice <= 0:  # inserir no início
            novo.próximo = self.__primeiro
            self.__primeiro = novo
        elif índice >= len(self):  # inserir no fim
            self.__último.próximo = novo

            self.__último = novo
        else:  # inserir entre dois elementos
            anterior = None
            atual = self.__primeiro

            i = 0
            while atual is not None:
                if i == índice:
                    anterior.próximo = novo
                    novo.próximo = atual
                    break

                anterior = atual
                atual = atual.próximo
                i += 1

        self.__tamanho += 1

    def index(self, x):
        atual = self.__primeiro

        i = 0
        while atual is not None:
            if atual.conteúdo == x:
                return i

            atual = atual.próximo
            i += 1

        raise ValueError('o elemento não faz parte da lista')
