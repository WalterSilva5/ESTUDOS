from listas_duplamente_ligadas import Lista

nomes = Lista()

nomes.inserir_início('Amaral')
nomes.inserir_fim('Leite')
nomes.inserir_início('Ygor')
nomes.inserir_fim('Sena')
nomes.inserir(2, 'Barbosa')
nomes.inserir(4, 'de')

for nome in nomes.inverso():
    print(nome)

print()
del nomes[0::2]
print()
# nomes.reverso()

for nome in nomes:
    print(nome)

print()
print(nomes)