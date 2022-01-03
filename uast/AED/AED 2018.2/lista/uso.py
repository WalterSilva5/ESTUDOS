from lista import Lista

pessoas = Lista()

# inserindo no início
pessoas.insert(0, 'Romário')
pessoas.insert(0, 'Victor')
pessoas.insert(0, 'Jonas')
pessoas.insert(0, 'Luiz')

# inserindo no fim
pessoas.insert(len(pessoas), 'Raimundo')
pessoas.insert(len(pessoas), 'Luiz W')
pessoas.insert(len(pessoas), 'Eduardo')

# temos 7 pessoas na lista

# inserindo no meio da lista
pessoas.insert(1, 'Jorge')
pessoas.insert(4, 'João P.')
pessoas.insert(6, 'Matheus')

pessoas.append('Jorge')
pessoas.append('Jorge')
pessoas.append('Jorge')
pessoas.append('Jorge')
print(pessoas.count('Jorge'))
print('{} foi removido com sucesso.'.format(pessoas.pop()))
print(pessoas)

#for i, pessoa in enumerate(pessoas):
#    print('{}ª - {}'.format(i+1, pessoa))

