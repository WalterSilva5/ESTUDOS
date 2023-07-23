import sys
class Encontrador(object):
    def __init__(self, valor):
        """esse programa deve resolver o problema passado na aula de calculo
        ex um numero elevado a si proprio é igual a 3
        sabemos que 1^1 = 1 < 3
        e 2^2 > 3
        então o valor esta entre 1 e 2"""
        sys.setrecursionlimit(99999)
        self.v = valor
        self.raiz = 1

    def calculaValor(self):
        if (self.raiz**self.raiz)<self.v:
            self.raiz+=0.0001
            self.calculaValor()
        else:
            print("{}".format(self.raiz))

e = Encontrador(3)
e.calculaValor()
