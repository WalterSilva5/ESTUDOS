class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None

    class No:
        def __init__(self, valor):
            self.pai = None
            self.esquerda = None
            self.direita = None
            self.valor = valor

        def __str__(self):
            return str(self.valor)

        def __repr__(self):
            return self.__str__()


    def inserir(self, valor):
        pai_atual = None
        atual = self.__raiz  # começando pela raiz
        novo = self.No(valor)  # criando o novo nó com o valor

        # vamos descer a partir da raiz
        # para encontrar a posição correta para inserir
        while atual is not None:
            pai_atual = atual

            # se o valor que queremos inserir for menor
            # ir para a sub-árvore da esquerda
            # caso contrário, ir para a sub-árvore da direita
            if novo.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        # o último pai encontrado será o pai do novo nó
        # caso não exista, o novo nó será a raiz da árvore
        novo.pai = pai_atual

        if pai_atual is None:
            # novo não tem pai, é o nó raiz
            self.__raiz = novo
        elif novo.valor < pai_atual.valor:
            # novo é menor que o pai, então é um filho a esquerda
            pai_atual.esquerda = novo
        else:
            # novo é maior que o pai, então é um filho a direita
            pai_atual.direita = novo


    def minimo(self, atual=None):
        # se atual não tem valor inicial, começar da raiz
        if atual is None:
            atual = self.__raiz

        # enquanto houver um filho a esquerda, caminhar nessa direção
        while atual.esquerda is not None:
            atual = atual.esquerda

        # não tem mais filho a esquerda
        # então atual é o menor elemento da árvore
        return atual

    def maximo(self, atual=None):
        # se atual não tem valor inicial, começar da raiz
        if atual is None:
            atual = self.__raiz

        # enquanto houver um filho a direita, caminhar nessa direção
        while atual.direita is not None:
            atual = atual.direita

        # não tem mais filho a direita
        # então atual é o maior elemento da árvore
        return atual

    def buscar(self, valor):
        atual = self.__raiz

        # enquanto atual existir e o valor for diferente do desejado
        # ir descendo na árvore pela esquerda (se for menor)
        # ou pela direita (se for maior)
        while atual is not None and valor != atual.valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        # se encontrou, atual é o próprio nó
        # caso contrário, atual é None
        return atual

    def buscar_recursivo(self, valor):

        def recursao(atual, valor):

            # é igual ou nulo?
            if valor == atual.valor or atual is None:
                # se encontrou, atual é o próprio nó buscado
                # caso contrário, atual é None
                return atual

            if valor < atual.valor:
                # se o valor buscado for menor que o atual
                # buscar na sub-árvore da esquerda
                return recursao(atual.esquerda, valor)
            else:
                # se o valor buscado for maior que o atual
                # buscar na sub-árvore da direita
                return recursao(atual.direita, valor)

        return recursao(self.__raiz, valor)

    def inserir(self, valor):
        pai_atual = None
        atual = self.__raiz  # começando pela raiz
        novo = self.No(valor)  # criando o novo nó com o valor

        # vamos descer a partir da raiz
        # para encontrar a posição correta para inserir
        while atual is not None:
            pai_atual = atual

            # se o valor que queremos inserir for menor
            # ir para a sub-árvore da esquerda
            # caso contrário, ir para a sub-árvore da direita
            if novo.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        # o último pai encontrado será o pai do novo nó
        # caso não exista, o novo nó será a raiz da árvore
        novo.pai = pai_atual

        if pai_atual is None:
            # novo não tem pai, é o nó raiz
            self.__raiz = novo
        elif novo.valor < pai_atual.valor:
            # novo é menor que o pai, então é um filho a esquerda
            pai_atual.esquerda = novo
        else:
            # novo é maior que o pai, então é um filho a direita
            pai_atual.direita = novo

    def sucessor(self, valor):
        atual = self.buscar(valor)

        # se o elemento não existe, não possui sucessor
        if atual is None:
            return atual

        # se existir uma sub-árvore a direita
        # o sucessor será o elemento da extrema esquerda dessa sub-árvore
        if atual.direita is not None:
            # (é uma busca de cima pra baixo)
            return self.minimo(atual.direita)

        # caso contrário...
        # o sucessor será o ancestral mais próximo (nós acima)
        # cujo o seu filho a esquerda também seja o ancestral do elemento informado (ou o próprio elemento informado)
        # se não existir esse ancestral, não possui sucessor
        # (é uma busca de baixo pra cima)
        # -----
        # subindo a árvore em busca do sucessor...
        pai_atual = atual.pai

        # enquanto atual ainda tiver pai (não chegar na raiz)
        # e atual for filho a direita... continuar buscando...
        # até atual ser filho a esquerda (encontrou sucessor)
        # ou não existir mais pai (sem sucessor)
        while pai_atual is not None and atual == pai_atual.direita:
            # subindo um nível hierárquico por repetição
            atual = pai_atual
            pai_atual = pai_atual.pai

        # sem sucessor
        if pai_atual is None:
            return pai_atual

        # com sucessor
        return pai_atual

    def predecessor(self, valor):
        atual = self.buscar(valor)

        # se o elemento não existe, não possui predecessor
        if atual is None:
            return atual

        # se existir uma sub-árvore a esquerda
        # o predecessor será o elemento da extrema direita dessa sub-árvore
        if atual.esquerda is not None:
            # (é uma busca de cima pra baixo)
            return self.maximo(atual.esquerda)

        # caso contrário...
        # o predecessor será o ancestral mais próximo (nós acima)
        # cujo o seu filho a direita também seja o ancestral do elemento informado (ou o próprio elemento informado)
        # se não existir esse ancestral, não possui predecessor
        # (é uma busca de baixo pra cima)
        # -----
        # subindo a árvore em busca do predecessor...
        pai_atual = atual.pai

        # enquanto atual ainda tiver pai (não chegar na raiz)
        # e atual for filho a esquerda... continuar buscando...
        # até atual ser filho a direita (encontrou predecessor)
        # ou não existir mais pai (sem predecessor)
        while pai_atual is not None and atual == pai_atual.esquerda:
            # subindo um nível hierárquico por repetição
            atual = pai_atual
            pai_atual = pai_atual.pai

        # sem predecessor
        if pai_atual is None:
            return pai_atual

        # com predecessor
        return pai_atual

    def apagar(self, valor):
        # se o nó a ser removido:
        # - não tiver filhos, simplesmente remover ele
        # - tem apenas um filho, arrastar o filho para o lugar dele
        # - tivar dois filhos... aí complica =D
        # -- nesse caso, iremos encontrar o sucessor do elemento a ser removido
        # -- o sucessor só terá no máximo um filho (a direita)
        # -- o sucessor será recortado (sem o filho) para o lugar do elemento a ser removido
        # -- o filho (se existir) do sucessor será filho agora do que era "avô"
        sera_removido = self.buscar(valor)

        if sera_removido.esquerda is None:
            # se não tem filho a esquerda, o filho a direita (se existir) vai para o seu lugar
            self.recortar(sera_removido, sera_removido.direita)
        elif sera_removido.direita is None:
            # nesse caso, só tem filho a esquerda
            # esse filho vai para o seu lugar
            self.recortar(sera_removido, sera_removido.esquerda)
        else:
            # o nó a ser removido possui dois filhos
            # deve-se encontrar o seu sucessor para recortá-lo
            # impossível esse sucessor ter filho a esquerda
            sucessor = self.sucessor(sera_removido.valor)

            if sucessor.pai != sera_removido:
                # o sucessor não está diretamente conectado com o que será removido
                # nesse caso, o filho da direita (se existir), será filho do que era "avô"
                self.recortar(sucessor, sucessor.direita)

                # como o sucessor irá subir para o nó que será removido
                # o filho a direita (que ficou órfão) será repassado/adotado
                sucessor.direita = sera_removido.direita
                # como o filho foi repassado, atualizando o novo pai (no filho órfão)
                sucessor.direita.pai = sucessor

            # movendo/recortando o sucessor para o lugar do nó removido
            self.recortar(sera_removido, sucessor)

            # a sub-árvore da esquerda do nó recortado será a que pertencia ao nó removido
            sucessor.esquerda = sera_removido.esquerda
            sucessor.esquerda.pai = sucessor

    # recorta um nó para o lugar do nó removido (o pai do recortado é atualizado)
    # o nó recortado não carrega os filhos
    def recortar(self, sera_removido, sera_recortado):
        if sera_removido.pai is None:
            # se o nó a ser removido não tiver pai, a raiz está sendo removida
            # o nó que será colocado no lugar será a nova raiz
            self.__raiz = sera_recortado
        elif sera_removido == sera_removido.pai.esquerda:
            # removendo um nó que é o filho a esquerda
            sera_removido.pai.esquerda = sera_recortado
        else:
            # removendo um nó que é o filho a direita
            sera_removido.pai.direita = sera_recortado

        if sera_recortado is not None:
            # o pai do que foi removido será pai agora do nó que foi para seu lugar
            sera_recortado.pai = sera_removido.pai

    def listar(self):
        # irá retornar uma lista ordenada
        lista = []

        # começa da raiz e desce até o elemento da extrema esquerda (mínimo)
        # irá buscar os elementos de baixo pra cima, da esquerda pra direita
        def em_ordem(atual):
            # atual é sempre uma raiz de uma sub-árvore qualquer
            # a raiz é cadastrada depois de seus descendentes da esquerda
            # e antes de seus descententes da direita
            # sub-árvore-esquerda < raiz <= sub-árvore-direita
            if atual is not None:
                # só cadastrará atual após toda a sua
                # sub-árvore da esquerda (números menores) ter sido cadastrada
                em_ordem(atual.esquerda)
                # toda a sub-árvore da esquerda foi cadastrada
                lista.append(atual.valor)  # cadastrando atual
                # cadastrando a sua sub-árvore da direita (números maiores)
                em_ordem(atual.direita)

        em_ordem(self.__raiz)

        return lista


arvore = ArvoreBuscaBinaria()

# arvore.inserir(5)
# arvore.inserir(8)
# arvore.inserir(9)
# arvore.inserir(7)
# arvore.inserir(6)
# arvore.inserir(2)

arvore.inserir(15)
arvore.inserir(6)
arvore.inserir(3)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(7)
arvore.inserir(13)
arvore.inserir(9)
arvore.inserir(18)
arvore.inserir(17)
arvore.inserir(20)

print('O maior elemento da árvore é: {}'.format(arvore.maximo()))
print('O menor elemento da árvore é: {}'.format(arvore.minimo()))
# arvore.apagar(15)


# print(arvore.buscar_recursivo(17))

print(arvore.apagar(15))
print(arvore.listar())
