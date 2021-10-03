#@author = walter pereira da silva lira
vendedores = []
while True:
    dicionario = {
        "salario":1219.0
    }
    dicionario["nome"]=input("Nome: ")
    if dicionario["nome"] == "parar":
        break
    dicionario["carros_vendidos"]=int(input("Quantidade de carros vendidos: "))
    for carro in range(dicionario["carros_vendidos"]):
        valor = float(input("Digite o valor do carro {}: ".format(carro+1)))
        dicionario["salario"]+=(valor/100)
    vendedores.append(dicionario)

print("#Relatorio#")
for vendedor in vendedores:
    print("{} ganhou R$:{:.2f}".format(vendedor["nome"],vendedor["salario"]))
