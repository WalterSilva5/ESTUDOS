from .first_script import valor_inteiro

def test_valor_inteiro():
    assert valor_inteiro(1) == 2
    assert valor_inteiro(2) == 3
    assert valor_inteiro(3) == 5
