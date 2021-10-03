import pickle

arquivo = open('banco.pck', 'rb')
clientes = pickle.load(arquivo)
arquivo.close()

#for cliente in clientes:
#    print(cliente)

for cliente in clientes:
    print(cliente["cpf"])