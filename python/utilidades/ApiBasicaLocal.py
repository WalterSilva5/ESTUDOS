import sys

class Teste():
    def printarArgs(self):
        for arg in sys.argv:
            print(arg)
            

teste=Teste()
teste.printarArgs()
