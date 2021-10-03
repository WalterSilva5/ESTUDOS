from carro import Carro
from barco import Barco
from abstractfactory import AbstractFactory

class VeiculoFactory(AbstractFactory):
    def criar_veiculo(self, obj):
        if obj == "barco":
            return Barco()
        if obj == "carro":
            return Carro()
            