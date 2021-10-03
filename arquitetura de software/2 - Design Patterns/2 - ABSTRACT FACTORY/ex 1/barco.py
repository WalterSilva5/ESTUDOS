from veiculo import Veiculo

class Barco(Veiculo):
    def __init__(self) -> None:
        super().__init__()
        
    def transportar(self):
        print("TRANSPORTANDO PELA AGUA")