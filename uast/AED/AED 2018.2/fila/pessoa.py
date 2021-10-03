class Pessoa:
    def __init__(self, nome='Desconhecido'):
        print('uma pessoa acabou de ser instanciada')
        self.nome = nome

    def cadastrar_mãe(self, mãe = 'Desconhecida'):
        self.mãe = mãe


pessoa1 = Pessoa('Romário')  # instanciando
# pessoa2 = Pessoa('João', '321.654.987-78', 'Outra mãe') # instanciando

print(id(pessoa1))
# print(id(pessoa2))

pessoa1.cadastrar_mãe('Maria')

print('O nome da pessoa1 é: {}'.format(pessoa1.nome))
print('O nome da mãe da pessoa1 é: {}'.format(pessoa1.mãe))
# print('O nome da pessoa2 é: {}'.format(pessoa2.nome))
