import pickle

clientes = [{'nome':'a', 'cpf':123456789, 'agencia': 1,'saldo':0.00},
            {'nome':'b', 'cpf':987654321, 'agencia': 2,'saldo':1.00}
            ]

arquivo = open('banco.pck', 'wb')
pickle.dump(clientes, arquivo)

arquivo.close()

