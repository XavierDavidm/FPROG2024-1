#3. Matriz identidade, na matemática, também conhecida como matriz 𝐼 ou matriz unitária, é uma
#matriz quadrada em que a diagonal principal contém apenas elementos 1 (um) e todos os outros
#elementos são 0 (zero). Crie uma função que gere uma matriz identidade 4x4

MI=[]



def GerarMatrixIdentidade():
    for x in range(4):
        novaLinha=[]
        for y in range(4):
            novoElemento=0
            novaLinha.append(novoElemento)
        MI.append(novaLinha)
        return MI


GerarMatrixIdentidade()
for x in range(len(MI)):
    for y in range(len(MI[0])):
        print(MI[x][y], end='\t')
    print()