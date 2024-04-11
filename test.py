num=0
numR=0
nLido=0
numS=0
n=int(input('informe quantos números devem ser lidos: '))
print(n,'números serão lidos abaixo')
while nLido<n:
    numR=float(input('digite um número: '))
    nLido=nLido+1
    print(nLido,')',numR)
    numS=numS+numR
print('a soma de todos os',n,'números é',numS)



