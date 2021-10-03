from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self) -> None:
        super().__init__()
        
    def transportar(self):
        print("TRANSPORTANDO PELA ESTRADA")