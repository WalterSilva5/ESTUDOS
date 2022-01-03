from lista_ligada import Lista

nomes = Lista()

nomes.inserir(len(nomes), 'Ygor')
nomes.inserir(len(nomes), 'Amaral')
nomes.inserir(len(nomes), [1,2,3,4])
nomes.inserir(len(nomes), {'nome': 'Flávio', 'disciplina': 'AED'})
nomes.inserir(len(nomes), 1000000)
nomes.inserir(len(nomes), 7.5)
nomes.inserir(len(nomes), 'Barbosa')

nomes.inserir(1, 'UFRPE')

nomes.inserir(0, 'Início')

for i, nome in enumerate(nomes):
    print('{} - {}'.format(i, nome))

print(len(nomes))

del nomes[7]

print(nomes[::])
