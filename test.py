import random
d2=random.randint(1,2)
d4=random.randint(1,4)
d6=random.randint(1,6)
d8=random.randint(1,8)
d12=random.randint(1,12)
d16=random.randint(1,16)
dadoescolhido=0
while dadoescolhido!=2 and dadoescolhido!=4 and dadoescolhido!=6 and dadoescolhido!=8 and dadoescolhido!=12 and dadoescolhido!=16:
    dadoescolhido=int(input('qual escolha o dado que deseja simular,(2,4,6,8,12 ou 16 lados): '))
    if dadoescolhido == 2:
        print('você jogou um Dado de 2 lados e o resultado foi',d2)
    elif dadoescolhido == 4:
        print('você jogou um Dado de 4 lados e o resultado foi',d4)
    elif dadoescolhido == 6:
        print('você jogou um Dado de 6 lados e o resultado foi',d6)
    elif dadoescolhido == 8:
        print('você jogou um Dado de 8 lados e o resultado foi',d8)
    elif dadoescolhido == 12:
        print('você jogou um Dado de 12 lados e o resultado foi',d12)
    elif dadoescolhido == 16:
        print('você jogou um Dado de 16 lados e o resultado foi',d16)
    else:
        print('O dado escolhido não é valido! por favor escolha outro dado listado')