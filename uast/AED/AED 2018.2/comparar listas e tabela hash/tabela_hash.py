class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__qnt_elementos = 0
        self.__tabela = []
        self.__inicializar_tabela()
        print()

    class Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        chaves = []
        for lista in self.__tabela:
            for elemento in lista:
                chaves.append(elemento.chave)

        return chaves

    def values(self):
        valores = []
        for lista in self.__tabela:
            for elemento in lista:
                valores.append(elemento.valor)

        return valores

    def items(self):
        itens = []
        for lista in self.__tabela:
            for elemento in lista:
                tupla = elemento.chave, elemento.valor
                itens.append(tupla)

        return itens

    def __len__(self):
        return self.__qnt_elementos

    def __contains__(self, key):
        índice = hash(key) % self.__tamanho

        for elemento in self.__tabela[índice]:
            if elemento.chave == key:
                return True

        return False

    def __getitem__(self, key):
        índice = hash(key) % self.__tamanho

        for elemento in self.__tabela[índice]:
            if elemento.chave == key:
                return elemento.valor

        raise KeyError(key)

    def __setitem__(self, key, value):
        índice = hash(key) % self.__tamanho

        if key in self:
            # vou atualizar
            for elemento in self.__tabela[índice]:
                if elemento.chave == key:
                    elemento.valor = value
                    return  # já atualizou, para de percorrer
        else:
            # vou inserir
            novo_elemento = self.Elemento(key, value)
            self.__tabela[índice].append(novo_elemento)
            self.__qnt_elementos += 1

    def __delitem__(self, key):
        índice = hash(key) % self.__tamanho

        for i, elemento in enumerate(self.__tabela[índice]):
            if elemento.chave == key:
                # elemento encontrado, apagando da lista interna
                del self.__tabela[índice][i]
                self.__qnt_elementos -= 1
                return  # já apagou, para de percorrer

        raise KeyError(key)

    def __str__(self):
        retorno = '{'

        i = 0
        for chave, valor in self.items():
            retorno += chave.__repr__()
            retorno += ': '
            retorno += valor.__repr__()

            if i < len(self) - 1:
                retorno += ', '

            i += 1

        retorno += '}'

        return retorno

    def __repr__(self):
        return self.__str__()

    def __inicializar_tabela(self):
        for i in range(self.__tamanho):
            self.__tabela.append([])


notas = TabelaHash(8)
pessoa = TabelaHash(4)

notas['1va'] = 10
notas['2va'] = 9
notas['3va'] = 'F'

pessoa['nome'] = 'Romário'
pessoa['idade'] = 18
pessoa['profissão'] = 'Estudante'
pessoa['notas'] = notas

#print(pessoa.keys())
#print(len(pessoa))

#for e in pessoa.items():
    #print(e)

print(pessoa)
print(type(pessoa['notas']))
# print(pessoas['nome'])
