class Pessoa():

    def __init__(self, nome, idade):
        self.__nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.__nome + ' personalizado'

    @nome.setter
    def nome(self, valor):
        self.__nome = 'novo nome ' + valor

pessoa1 = Pessoa('João da Silva', 40)


print('O nome dessa pessoa1 é {}'.format(pessoa1.nome))
pessoa1.nome = 'José da Silva'
print('O nome dessa pessoa1 é {}'.format(pessoa1.nome))