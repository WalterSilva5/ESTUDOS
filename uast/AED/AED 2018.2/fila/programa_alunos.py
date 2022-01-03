from aluno import Aluno


def menu():
    print('1 - Cadastrar')
    print('2 - Mostrar')
    print('3 - Sair')

    op = int(input('>>> '))

    return op


def cadastrar_aluno(alunos):
    nome = input('Digite o nome do aluno: ')
    cpf = input('Digite o cpf do aluno: ')

    try:
        nota = float(input('Digite a nota do aluno: '))
    except ValueError:
        nota = None

    novo_aluno = Aluno(nome, cpf, nota)

    alunos.append(novo_aluno)


def mostrar_alunos(alunos):
    if len(alunos) > 0:
        print('-=' * 20)
        print(' ALUNOS CADASTRADOS')
        print('-=' * 20)
        for i, aluno in enumerate(alunos, 1):
            print('Aluno: {}'.format(i))
            print('\tNome: {}'.format(aluno.nome))
            print('\tCPF: {}'.format(aluno.cpf))
            print('\tNota: {}\n'.format(aluno.tem_nota()))
        print('-=' * 20)
    else:
        print('Nenhum aluno foi cadastrado ainda.')

    print('\n')


alunos = []

while True:
    op = menu()

    if op == 1:
        cadastrar_aluno(alunos)
    elif op == 2:
        mostrar_alunos(alunos)
    elif op == 3:
        print('Saindo do programa. Obrigado.')
    else:
        print('Opção inválida. Por favor, tente novamente.')
