class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Atleta(Pessoa):
    def __init__(self, nome, idade):
        super(Atleta, self).__init__(nome, idade)
        
    
teste = Atleta('walter', 24)
print(teste.nome)