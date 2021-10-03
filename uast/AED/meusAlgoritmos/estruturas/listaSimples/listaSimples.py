class Lista():
    def __init__(self):
        self.__inicio = None
        self.__tam = 0
        
    class No:
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None
            
    def adicionar(self, valor):
        no = self.No(valor)
        
        if self.__inicio is None:
            self.__inicio = no
        else:
            perc = self.__inicio
            while perc.proximo is not None:
                perc=perc.proximo
            perc.proximo = no
        self.__tam +=1
        
    def inserir(self):
        
        
    def __str__(self):
        pass