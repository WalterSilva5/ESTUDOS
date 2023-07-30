import pytest
from script_aula3 import Restaurante

@pytest.fixture
def restaurante_zerado():
    return Restaurante("teste", 0)

@pytest.fixture
def restaurante_com_valor():
    return Restaurante("teste", 3)

def test_remove_pedido(restaurante_zerado, restaurante_com_valor):
    with pytest.raises(ValueError):
        restaurante_zerado.remover_pedido()
    restaurante_com_valor.remover_pedido()
