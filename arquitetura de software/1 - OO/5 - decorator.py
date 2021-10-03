#criando um decorator que transforma as strings recebidas como parametro de um metodo em maiusculas

class maiusculas(object):
    def __init__(self, f):
        self.f = f
    
    def __call__(self, *args):
        self.f(args[0].upper())

@maiusculas
def nome(texto):
    print("Nome: ",texto)
    
nome("walter")