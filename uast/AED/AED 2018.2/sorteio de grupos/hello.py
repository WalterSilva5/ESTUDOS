def repetir(ate, i=0):
    # condição de parada ou existência
    if i <= ate:
        print('{}'.format(i))
        repetir(ate, i + 1) # passo recursivo


repetir(10) #chamando a função recursiva

i = 0
while i <= 10:
    print('{}'.format(i))
    i += 1
