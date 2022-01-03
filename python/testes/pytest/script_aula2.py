class Restaurante():
    def __init__(self, nome, tamanho_fila):
        self.nome = nome
        self.tamanho_fila = tamanho_fila
    @property
    def tamanho_fila(self):
        return self._tamanho_fila

    @tamanho_fila.setter
    def tamanho_fila(self, tamanho_fila):
        if tamanho_fila < 0:
            raise ValueError("Tamanho da fila deve ser maior que zero")        
        else:
            self._tamanho_fila = tamanho_fila

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def adiciona_pedido(self):
        self.tamanho_fila += 1
        
    def remover_pedido(self):
        if self.tamanho_fila >0:
            self.tamanho_fila -= 1
