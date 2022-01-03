class cadastro():
    def __init__(self,nome,cpf,idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

pessoas = []

while True:
    nome = input("Nome: ").title()
    if nome == "Parar" or nome == "Sair":
        break
    cpf = input("Cpf: ")
    idade = input("Idade: ")
    pessoa = cadastro(nome,cpf,idade)

    pessoa = pessoa.__dict__
    if int(pessoa["idade"])>=65:
        pessoas.insert(pessoas[0],pessoa)
    else:
        pessoas.append(pessoa)

print (pessoas)
while True:
    print("1- Agendar paciente")
    print("2- atender o proximo")
    print("3- mostrar A fila de atendimento")
    print("4- Sair do Programa")

    op = int(input("Opção: "))

    if op == 4:
        break

    elif op ==1:
        cpfAgendamento = input("CPF: ")
        for x in range(len(pessoas)):
            if pessoas[x]["cpf"]==cpfAgendamento:
                print("{} agendado".format(pessoas[x]["nome"]))
