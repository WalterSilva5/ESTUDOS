class Fila:
    def __init__(self):
        self.__fila = []

    def enfileirar(self, nome):
        self.__fila.append(nome)

    def desenfileirar(self):
        return self.__fila.pop(0)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.desenfileirar()
        except IndexError:
            raise StopIteration


    def __len__(self):
        return len(self.__fila)



fila = Fila()

fila.enfileirar('Romário')
fila.enfileirar('Victor')
fila.enfileirar('Flávio')
fila.enfileirar('Luiz')

print('Quantidade de pacientes na fila: {}'.format(len(fila)))

for paciente in fila:
    print('{} foi atendido'.format(paciente))


print('Todos os pacientes foram atendidos')