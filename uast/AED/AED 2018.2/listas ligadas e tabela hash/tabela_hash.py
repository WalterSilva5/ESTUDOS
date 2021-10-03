class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho  # tamanho da tabela, não tem relação com qnt de elementos
        self.__qnt_elementos = 0  # quantidade de elementos armazenados na tabela
        self.__tabela = []
        self.__inicializar_tabela()

    # representação interna dos elementos que serão armazenados na tabela hash
    class Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor

    # retorna todas as chaves inseridas na tabela
    def keys(self):
        chaves = []
        for lista in self.__tabela:
            for elemento in lista:
                chaves.append(elemento.chave)

        return chaves

    # retorna todos os valores inseridos na tabela
    def values(self):
        valores = []
        for lista in self.__tabela:
            for elemento in lista:
                valores.append(elemento.valor)

        return valores

    # retorna todos os itens (elementos chave/valor) inseridos na tabela
    def items(self):
        itens = []
        for lista in self.__tabela:
            for elemento in lista:
                tupla = elemento.chave, elemento.valor
                itens.append(tupla)

        return itens

    # é iterável
    def __iter__(self):
        # a tabela hash itera sobre a lista que guarda as chaves
        return iter(self.keys())

    # retorna a quantidade de elementos armazenados (ao invés do tamanho da tabela)
    def __len__(self):
        return self.__qnt_elementos

    # verifica se a chave existe
    def __contains__(self, key):
        try:
            self.__pegar_elemento_interno(key)
            return True
        except KeyError:
            return False

    # recupera o valor associado a uma determinada chave
    def __getitem__(self, key):
        elemento = self.__pegar_elemento_interno(key)
        return elemento.valor

    # insere ou atualiza o valor associado a uma determinada chave
    def __setitem__(self, key, value):
        self.__atualizar_chave(key, value)

    # deletar o elemento que possui uma determinada chave
    def __delitem__(self, key):
        índice = self.__função_hash(key)
        for i, elemento in enumerate(self.__tabela[índice]):
            if elemento.chave == key:
                # achou a chave, remover esse elemento que está na posição i
                del self.__tabela[índice][i]
                self.__qnt_elementos -= 1
                return  # já achou e deletou, sair da função

        # chave não existe, gerar um KeyError
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

    # método privado para recuperar o objeto elemento (que possui chave - valor)
    def __pegar_elemento_interno(self, key):
        índice = self.__função_hash(key)
        for elemento in self.__tabela[índice]:
            if elemento.chave == key:
                # achou a chave, retornar o objeto elemento (e não apenas o valor)
                return elemento

        # chave não existe, gerar um KeyError
        raise KeyError(key)

    # método privado para atualizar o valor da chave
    def __atualizar_chave(self, key, value):
        try:
            # se a chave já tiver sido criada, sobrescrever o seu valor
            elemento = self.__pegar_elemento_interno(key)  # recuperando o elemento para modificar o seu valor
            elemento.valor = value
        except KeyError:
            # chave ainda não existe, inserir uma nova chave
            índice = self.__função_hash(key)
            novo_elemento = self.Elemento(key, value)
            self.__tabela[índice].append(novo_elemento)
            self.__qnt_elementos += 1  # só incrementa ao inserir (qnd atualizar mantém o valor)

    # método privado para inicializar todos os índices da tabela com uma lista vazia
    def __inicializar_tabela(self):
        for i in range(self.__tamanho):
            self.__tabela.append([])

    # retorna em qual índice da tabela a chave deverá ser armazenada/recuperada
    def __função_hash(self, chave):
        return hash(chave) % self.__tamanho


notas = TabelaHash(11)
pessoa = TabelaHash(11)

notas['1va'] = 7.9
notas['2va'] = 7.2
notas['3va'] = 8.6

pessoa['nome'] = 'Ygor'
pessoa['nome'] = 'João'
pessoa['idade'] = 31
pessoa['profissão'] = 'Professor'
pessoa['notas'] = notas

print(pessoa['profissão'])
print(len(pessoa))
print('nom' in pessoa)
print(pessoa)
print()
for e in pessoa.items():
    print(e)

# aluno = {'nome': 'Fulano da Silva', 'idade': 30}
#
# for e in aluno.values():
#     print(e)
