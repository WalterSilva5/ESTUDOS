"""
codigos no github se precisar conferir os commits
https://github.com/WalterSilva5/uast/tree/master/INTRODU%C3%87%C3%83O%20A%20PROGRAMA%C3%87%C3%83O/Projeto%202%20va
"""
def testa_banco():
    try:
        arquivo = open("banco.txt", "r")
    except Exception:
        arquivo = open("banco.txt", "w")
    finally:
        arquivo.close()
def tela_inicial():
    try:
        op = int (input("""
            #####SISTEMA BANCARIO ####
0 - SAIR        
1 - CRIAR CONTA
2 - ALTERAR  CADASTRO            
3 - LISTAR CLIENTES
4 - BUSCAR CLIENTE
5 - DELETAR CLIENTE
6 - FAZER DEPOSITO
7 - SACAR VALOR

Digite o numero da opção escolhida: """))
    except Exception:
        print("DIGITE UMA OPÇÃO VALIDA\nTENTE NOVAMENTE")
        tela_inicial()
    if op == 0:
        print("FIM DO PROGRAMA.")
        exit()
    if op == 1:
        cadastrar()
    elif op ==2:
        altera_cliente()
    elif op ==3:
        listar_clientes()
        tela_inicial()
    elif op == 4:
        busca_cliente()
    elif op == 5:
        exclui_cliente()
    elif op == 6:
        fazer_deposito()
    elif op == 7:
        fazer_saque()
    else:
        print("Digite uma opção valida\nTENTE NOVAMENTE")
        tela_inicial()
def fazer_deposito():
    clientes = ler_clientes()
    quicksort(clientes, 0, len(clientes) - 1)
    print("OPÇÃO - FAZER DEPOSITO")
    cpf = recebe_cpf()
    posicao = busca_binaria(clientes, 0, len(clientes) - 1, cpf)
    if posicao >= 0:
        while True:
            valor = float(input("VALOR DO DEPOSITO:"))
            if valor<=0:
                print("O VALOR DE DEPOSITO DEVE SER MAIOR QUE ZERO")
                continue
            else:
                clientes[posicao]["saldo"]+=valor
                salva_cliente(clientes)
                print("DEPOSITO CONCLUIDO O NOVO SALDO DO CLIENTE É DE R$: {:.2f} O ANTIGO ERA {:.2f}".format(clientes[posicao]["saldo"],
                                                                                                              clientes[posicao]["saldo"]-valor))
                tela_inicial()
    else:
        print("CPF NÃO CADASTRADO TENTE NOVAMENTE")
        fazer_deposito()
def fazer_saque():
    clientes = ler_clientes()
    quicksort(clientes, 0, len(clientes) - 1)
    print("OPÇÃO - FAZER SAQUE")
    cpf = recebe_cpf()
    posicao = busca_binaria(clientes, 0, len(clientes) - 1, cpf)
    if posicao >= 0:
        while True:
            print("SALDO ATUAL DA CONTA R$:{:.2f}".format(clientes[posicao]["saldo"]))
            valor = float(input("VALOR DO SAQUE:"))
            if valor<=0:
                print("O VALOR DE SAQUE DEVE SER MAIOR QUE ZERO")
                continue
            if valor > clientes[posicao]["saldo"]:
                print("O VALOR DO SAQUE DEVE SER MENOR QUE O SEU SALDO EM CONTA.")
            else:
                clientes[posicao]["saldo"]-=valor
                salva_cliente(clientes)
                print("SAQUE CONCLUIDO O NOVO SALDO DA CONTA É DE R$: {:.2f} O ANTIGO ERA {:.2f}".format(clientes[posicao]["saldo"],
                                                                                                              clientes[posicao]["saldo"]+valor))
                tela_inicial()
    else:
        print("CPF NÃO CADASTRADO TENTE NOVAMENTE")
        fazer_deposito()
#parte que cadastra cliente
def cadastrar():
    print("ENTRE COM AS INFORMAÇÕES DO CLIENTE.")
    nome = input("NOME: ").upper()
    #parte so pra entrada do cpf
    cpf = recebe_cpf()
    if cpf_cadastrado(cpf)>=0:
        print("ESSE CPF JA ESTA CADASTRADO!")
        tela_inicial()
    #entrada da agencia
    agencia = recebe_agencia()

    clientes = ler_clientes()
    clientes.append({'nome':nome, 'cpf':cpf, 'agencia':agencia, 'saldo': 0.00})
    salva_cliente(clientes)
#parte de alterar cadastro
def altera_cliente():
    cpf = recebe_cpf()
    if cpf_cadastrado(cpf):
        clientes = ler_clientes()
        for cliente in range(len(clientes)):
            if clientes[cliente]["cpf"]==cpf:
                print("INSIRA AS NOVAS INFORMAÇÕES DO CLIENTE")
                clientes[cliente]["nome"]= input("NOME: ")
                clientes[cliente]["agencia"] = recebe_agencia()
        salva_cliente(clientes)
    else:
        print("ESSE CPF NÃO ESTÁ CADASTRADO!")
        tela_inicial()
#buscar cliente
def busca_cliente():
    clientes = ler_clientes()
    quicksort(clientes, 0, len(clientes)-1)
    cpf = recebe_cpf()
    posicao = busca_binaria(clientes, 0, len(clientes)-1, cpf)
    if posicao >= 0:
        print("""
                CLIENTE ENCONTRADO!
        NOME: {}
        CPF: {}
        AGENCIA: {}
        SALDO: {}
                """.format(clientes[posicao]["nome"], clientes[posicao]["cpf"], clientes[posicao]["agencia"], clientes[posicao]["saldo"]))
    else:
        print("CPF NÃO CADASTRADO!")
    tela_inicial()
#deleta cliente
def exclui_cliente():
    clientes = ler_clientes()
    quicksort(clientes, 0, len(clientes)-1)
    cpf = recebe_cpf()
    posicao = busca_binaria(clientes, 0, len(clientes)-1, cpf)
    if posicao>=0:
        confirma = input("DESEJA REALMENTE EXCLUIR ESSE CPF?[S/N]: ").upper()
        if confirma == 'S':
            del(clientes[posicao])
            salva_cliente(clientes)
            print("OPERÇÃO CONCLUIDA - CLIENTE DELETADO!")
        else:
            print("OPERÇÃO CANCELADA!")
    else:
        print("CPF NÃO CADASTRADO")
    tela_inicial()
#parte que lista os clientes
def listar_clientes():
    clientes = ler_clientes()
    if len(clientes)<=0:
        print("nenhum cliente cadastrado")
        tela_inicial()
    else:
        clientes_ord = clientes.copy()

        while True:
            print("""
Você deseja ordenar por qual característica?")
1 - CPF
2 - NOME
3 - AGENCIA
4 - SALDO
""")
            característica = int(input("?:"))
            if característica >= 1 or característica <= 3:
                break

            print("Opção inválida. Tente novamente.")

        while True:
            print("Em qual ordem deseja ordenar ?")
            print("1 - Crescente")
            print("2 - Decrescente")
            ordem = int(input("> "))
            if ordem >= 1 or ordem <= 2:
                break

            print("Opção inválida. Tente novamente.")
        quicksort(clientes_ord, 0, len(clientes_ord) - 1, característica, ordem)
        cont = 1
        print("######## CLIENTES ########")
        for cliente in clientes_ord:
            print("""##########################
CLIENTE {}
NOME: {}
CPF: {}
AGENCIA: {}
SALDO: {}""".format(cont, cliente["nome"], cliente["cpf"], cliente["agencia"], cliente["saldo"]))
            cont+=1
    print("\nTOTAL DE CLIENTES: {}".format(cont-1))
#funções adicionais que servem pras outras
def cpf_cadastrado(cpf):
    clientes = ler_clientes()
    if len(clientes)>0:
        quicksort(clientes, 0, len(clientes)-1)
        posicao = busca_binaria(clientes, 0, len(clientes)-1, cpf)
        if posicao>=0:
            return posicao
        else:
            return -1
    else:
        return -1

#recebem valores validos
def recebe_cpf():
    while True:
        try:
            print("o cpf deve ter 9 digitos numericos")
            print("Para sair digite -1")
            cpf = int(input("CPF: "))
            if cpf == -1:
                print("Operação cancelada")
                tela_inicial()
            elif len(str(cpf)) != 9:
                raise Exception
        except:
            print("Ocorreu um erro!\nDigite um cpf valido")
        else:
            return cpf
def recebe_agencia():
    while True:
        try:
            agencia = int(input("Numero da agencia - 'deve ser um numero de 0 a 9': "))
            if agencia<0 or agencia>9:
                raise Exception
        except Exception:
            print("O valor digitado é invalido ")
        else:
            return agencia
#salvam o arquivo
def salva_cliente(clientes):
    arquivo = open("banco.txt", "w")
    for c in clientes:
        arquivo.write("{}#{}#{}#{}\n".format(c["nome"], c["cpf"], c["agencia"], c["saldo"]))
    arquivo.close()
    print("ALTERAÇÕES SALVAS!")
    tela_inicial()

def ler_clientes():
    clientes = []
    arquivo = open("banco.txt", "r")
    lista = arquivo.readlines()
    for linha in lista:
        linha = linha.strip()
        linha = linha.split("#")
        clientes.append({'nome':linha[0], 'cpf':int(linha[1]), 'agencia':int(linha[2]), 'saldo':float(linha[3])})
    if len(clientes)== 0:
        return[]
    else:
        return(clientes)
#busca binaria
def busca_binaria(vetor, pos_inicial, pos_final, elemento):
    if pos_inicial <= pos_final:
        meio = (pos_inicial+pos_final)//2
        if elemento>vetor[meio]["cpf"]:
            return busca_binaria(vetor, meio+1, pos_final, elemento)
        elif elemento<vetor[meio]["cpf"]:
            return busca_binaria(vetor, pos_inicial, meio-1, elemento)
        else:
            #se cair aqui quer dizer que encontrou entao pode retornar a posicao do meio
            return meio
    return -1
#quick sort
def quicksort(clientes_ord, pos_inicial, pos_final, característica=1, ordem=1):
    if pos_inicial < pos_final:
        pivo = particionar(clientes_ord, pos_inicial, pos_final, característica, ordem)
        quicksort(clientes_ord, pos_inicial, pivo - 1, característica, ordem)
        quicksort(clientes_ord, pivo + 1, pos_final, característica, ordem)
def particionar(clientes, pos_inicial, pos_final, característica, ordem):
    pivo = clientes[pos_inicial]
    proxima_pos = pos_inicial
    contador = pos_inicial + 1
    while contador <= pos_final:
        chave = chave_ordenação(clientes, pivo, contador, característica, ordem)
        if chave:
            proxima_pos += 1
            trocar(clientes, proxima_pos, contador)
        contador += 1

    trocar(clientes, pos_inicial, proxima_pos)
    return proxima_pos
def chave_ordenação(clientes, pivo, j, característica, ordem):
    if característica == 1:
        chave = 'cpf'
    elif característica == 2:
        chave = 'nome'
    elif característica == 3:
        chave = 'agencia'
    elif característica == 4:
        chave = 'saldo'

    if ordem == 1:
        comparacao = clientes[j][chave] < pivo[chave]
    else:
        comparacao = clientes[j][chave] > pivo[chave]

    #retorna uma comparação por isso não precisa fazer a comparação no particionar do quick sort
    return comparacao
def trocar(clientes, x, y):
    clientes[x], clientes[y] = clientes[y], clientes[x]
#fim do quicksort
#garante que o banco exista
testa_banco()
#inicio do programa
tela_inicial()
