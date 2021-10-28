
import pytest
from script_aula2 import Restaurante

def test_pedidos_na_fila_valor_inicial():
    """
    Testa se o programa esta aceitando uma fila com 
    tamanho igual a zzero
    """
    restaurante = Restaurante('teste', 0)
    assert restaurante.tamanho_fila == 0
    
def test_pedidos_na_fila_valor_inicial_maior_que_zero():
    """
    Testa se o programa esta aceitando uma fila 
    com tamanho maior que zero
    """
    restaurante = Restaurante('teste', 1)
    assert restaurante.tamanho_fila == 1

def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    """
    Testa se o programa esta levantando uma exceção quando 
    o tamanho da fila é menor que zero
    """
    with pytest.raises(ValueError):
        restaurante = Restaurante('teste', -1)
        
def test_adiciona_pedido_a_fila():
    """
    Testa se o programa esta adicionando um pedido na fila
    """
    restaurante = Restaurante('teste', 1)
    restaurante.adiciona_pedido()
    assert restaurante.tamanho_fila == 2
def test_remover_pedido():
    """
    Testa se o programa esta removendo um pedido da fila
    """
    restaurante = Restaurante('teste', 1)
    restaurante.remover_pedido()
    assert restaurante.tamanho_fila == 0