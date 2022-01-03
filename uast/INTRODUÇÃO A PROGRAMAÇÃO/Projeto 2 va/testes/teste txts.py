arq = open("arquivo.txt", "w")
arq.write("""
a
b
c
""")
arq.close()
arq = open("arquivo.txt")
print(arq.readlines())
for linha in arq:
    print(linha.strip())
arq.close()