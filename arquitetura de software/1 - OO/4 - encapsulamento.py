class Pessoa(object):
    def __init__(self) -> None:
        super().__init__()
        self._nome = None
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        if len(nome)<6:
            print("nome invalido")
        else:
            self._nome = nome
            print("nome atribuido")
            
pessoa = Pessoa()
pessoa.nome = "wal"