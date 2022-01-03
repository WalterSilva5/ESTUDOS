from script_aula1 import valor_inteiro
import pytest


def test_valor_inteiro():
    # essa funcao deve receber um valor e retornar o valor + 1
    assert valor_inteiro(1) == 2
    assert valor_inteiro(2) == 3
    assert valor_inteiro(3) == 5

    assert valor_inteiro('2') == 3


def test_valor_inteiro_tipo():
    """
    * caso seja passado um valor que não possa ser
    convertido para inteiro deve levantar um erro
    o erro deve ser levantado
    """
    with pytest.raises(ValueError):
        valor_inteiro('value')
