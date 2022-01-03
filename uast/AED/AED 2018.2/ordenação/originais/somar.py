def algoritmoA(n):
    soma = 0
    i = 1
    while i <= n:
        soma += i
        i += 1

    return soma


def algoritmoB(n):
    soma = 0
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            soma += 1
            j += 1
        i += 1

    return soma


def algoritmoC(n):
    return int(n * (n + 1) / 2)



print(algoritmoA(10))
print(algoritmoB(10))
print(algoritmoC(10))