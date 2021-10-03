from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def transportar(self):
        pass
    
    