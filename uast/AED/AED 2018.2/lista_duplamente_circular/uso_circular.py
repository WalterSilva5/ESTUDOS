from listas_circulares_duplamente_ligadas import Lista

nomes = Lista()

nomes.inserir_início('Amaral')
nomes.inserir_fim('Leite')
nomes.inserir_início('Ygor')
nomes.inserir_fim('Sena')
nomes.inserir(2, 'Barbosa')
nomes.inserir(4, 'de')
nomes.inserir_fim('Acabou')

print(nomes)
print(len(nomes))

print()
for nome in nomes:
    print(nome)
