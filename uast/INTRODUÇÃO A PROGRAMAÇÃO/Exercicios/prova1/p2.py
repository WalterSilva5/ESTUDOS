for x in range (1,201):
    divisores = 0
    for j in range(1,x+1):
        if x%j == 0:
            divisores+=1
    if divisores == 6:
        print("\nnumero: {}\ndivisores:\n".format(x))
        for j in range(1,x+1):
            if x%j == 0:
                print(j)
