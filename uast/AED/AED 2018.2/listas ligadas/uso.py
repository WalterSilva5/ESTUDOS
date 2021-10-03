from listas_ligadas import Lista


nomes = Lista(['Ygor', 'Amaral', 'Barbosa', 'Leite', 'de', 'Sena'])

print(nomes)

for i, e in enumerate(nomes):
    print('i - {} | Nome: {}'.format(i, e))