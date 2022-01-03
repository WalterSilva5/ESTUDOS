matriz = []
listaN = []
cont = 0
maior = 0
for x in range(9):
    listaN.append(int(input("N {}: ".format(x+1))))
menor = listaN[1]

for x in range(1, len(listaN)):
    if listaN[x] < menor:
        menor = listaN[x]

for x in range(3):
    linha =[]
    matriz.append([])
    matriz[x] = linha
    for j in range(3):
        linha.append(listaN[cont])
        cont+=1

for x in range(3):
    for j in range(3):
        if matriz[x][j]== menor:
            maior = matriz[x][0]
            for k in range(len(matriz[x])):
                if matriz[x][k]>maior:
                    maior = matriz[x][k]

            for k in range(len(matriz[x])):
                if matriz[x][k]== maior:
                    print("linha {} coluna {} elemento {}".format(x+1, k+1, maior))
for x in range(3):
    str=""
    for j in range(3):
        str+="{}\t".format(matriz[x][j])
    print(str)