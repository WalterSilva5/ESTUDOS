class Pessoa():
    #estados
    nome = "Walter"
    idade = 24
    
    #comportamentos
    def alterar_idade (self, nova_idade):
        self.idade = nova_idade
        

pessoa = Pessoa()
print(pessoa.idade)
pessoa.alterar_idade(15)
print(pessoa.idade)