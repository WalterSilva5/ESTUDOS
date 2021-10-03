class Lista():
    def __init__(self):
        self.primeiro = None
        self.último = None
        self.__tamanho = 0
        self.__iterando = None

    class Nó():
        def __init__(self, conteúdo):
            self.conteúdo = conteúdo
            self.próximo = None

    def __len__(self):
        return self.__tamanho

    def __getitem__(self, i):
        atual = self.primeiro

        _índice_atual = 0
        while atual is not None:
            if _índice_atual == i:
                # encontrou o elemento desejado
                return atual.conteúdo

            # indo para o próximo elemento
            atual = atual.próximo
            _índice_atual += 1

        raise IndexError("list index out of range")

    def __setitem__(self, i, value):
        atual = self.primeiro

        _índice_atual = 0
        while atual is not None:
            if _índice_atual == i:
                # encontrou o elemento desejado
                atual.conteúdo = value
                return

            # indo para o próximo elemento
            atual = atual.próximo
            _índice_atual += 1

        raise IndexError("list index out of range")

    def __iter__(self):
        return self

    def __next__(self):
        # vai percorrer utilizando o conceito de lazy evaluating
        if self.__iterando is None:  # começando início / começando a iterar
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.próximo

        if self.__iterando is not None:
            return self.__iterando.conteúdo

        raise StopIteration

    def __delitem__(self, i):

        # se i está dentro da lista vai apagar, caso contrário, IndexError
        if i < len(self):
            atual = self.primeiro

            if i == 0:  # apagar o primeiro elemento
                self.primeiro = atual.próximo
                atual.próximo = None

                # apagando o primeiro/último elemento
                # último passará a ser o NONE
                if i == len(self) - 1:
                    self.último = None

            else:  # apagar elemento intermediário ou último
                anterior = None
                _índice_atual = 0
                while atual is not None:
                    if _índice_atual == i:
                        anterior.próximo = atual.próximo
                        atual.próximo = None

                        # apagando o último elemento
                        # último passará a ser o anterior
                        if i == len(self) - 1:
                            self.último = anterior

                        break

                    anterior = atual
                    atual = atual.próximo
                    _índice_atual += 1

            self.__tamanho -= 1

            self.__iterando = None

        else:
            raise IndexError("list index out of range")

    def __str__(self):
        retorno = '['
        for i, e in enumerate(self):
            retorno += e.__repr__()

            if i < len(self) - 1:
                retorno += ', '

        retorno += ']'

        return retorno

    def __repr__(self):
        return self.__str__()

    def append(self, x):
        self.insert(len(self), x)

    def insert(self, i, x):
        novo = self.Nó(x)

        # se a lista está vazia
        if self.primeiro is None:
            self.primeiro = novo
            self.último = novo
        elif i <= 0:  # inserir no início da lista
            # o novo vai apontar para o que ERA primeiro
            novo.próximo = self.primeiro

            # o novo torna-se o primeiro elemento
            self.primeiro = novo
        elif i >= len(self):  # inserir no final da lista

            # o que era último vai apontar para o novo
            self.último.próximo = novo

            # e o novo torna-se o último
            self.último = novo
        else:  # inserir um elemento intermediário
            atual = self.primeiro

            _índice_atual = 0
            while atual is not None:
                if _índice_atual == i - 1:
                    novo.próximo = atual.próximo
                    atual.próximo = novo
                    break

                atual = atual.próximo
                _índice_atual += 1

        self.__iterando = None
        self.__tamanho += 1

    # Return the number of times x appears in the list.
    def count(self, x):

        vezes = 0
        for e in self:
            if e == x:
                vezes += 1

        return vezes

    def index(self, x):
        for i, e in enumerate(self):
            if e == x:
                return i

        raise ValueError('{} is not in list'.format(x))

    # Remove the first item from the list whose value is equal to x.
    # It raises a ValueError if there is no such item.
    def remove(self, x):
        for i, e in enumerate(self):
            if e == x:
                del self[i]
                return

        raise ValueError('{} is not in list'.format(x))

    # Remove the item at the given position in the list, and return it.
    # If no index is specified,
    # a.pop() removes and returns the last item in the list.
    def pop(self, i = None):

        if i is None:
            i = len(self) - 1

        try:
            removido = self[i]
            del self[i]
            return removido
        except ValueError:
            pass

        raise IndexError('pop index out of range')