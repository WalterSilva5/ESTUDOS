from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def criar_veiculo(self, obj):
        pass
