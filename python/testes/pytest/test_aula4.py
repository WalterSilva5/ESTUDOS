import pytest
from script_aula4 import Restaurante

@pytest.mark.parametrize("inicial,final", [(0,0), (1,0), (2,1)] )
def test_remove_pedido(inicial, final):
    restaurante = Restaurante("teste", inicial)
    restaurante.remover_pedido()
    assert restaurante.tamanho_fila == final