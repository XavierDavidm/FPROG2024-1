#lista 04 while e for
#.1 Faça um algoritmo para:
#a. Gerar e escrever todos os números inteiros do intervalo [0,100].
#b. Gerar e escrever os números pares do intervalo [20,50].
#c. Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente.
#d. Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente.
#e. Ler 15 números e escrever a soma e a média dos números lidos.
#f. Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números
#ímpares lidos.
#g. Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem
#“POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de
#números positivos e negativos lidos.
#h. Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números
#que deverão ser lidos e também deve ser lido do teclado)

#1a)
for A in range(0,101):
    print(A)
print('#####')

#1B)
for B in range(20,51,2):
    print(B)
print('#####')

#1C)
for C in range(70,24,-1):
    print(C)
print('#####')

#1D)
for D in range(95,24,-2):
    print(D)
print('#####')

#1E)
numR=0
numS=0
cont=0

while cont<15:
    numR=float(input('digite um número: '))
    cont=cont+1
    print(cont,')',numR)
    numS=numS+numR
    numM=numS/15
print('a soma dos quinze números acima é',numS)
print('a média dos quinze números acima é',numM)

#1F) 
cont=0
numR=0
contP=0
contN=0

while cont<10:
    numR=int(input('digite um número inteiro: '))
    cont=cont+1
    print(cont,')',numR)
    if numR%2:
        contP=contP+1
    else:
        contN=contN+1
print('entre os 10 números digitados acima',contP,'são pares e',contN,'são ímpares')

#1G)
import random
nSort=0
num=0
contPOS=0
contNE=0
contNUL=0
while nSort<20:
    num=random.randint(-10,10)
    if num < 0:
        print(num,'é negativo')
        contNE=contNE+1
    elif num == 0:
        print(num,'é nulo')
        contNUL=contNUL+1
    else:
        print(num,'é positivo')
        contPOS=contPOS+1
    nSort=nSort+1
print('entre os 20 números sorteados',contPOS,'são positivos',',',contNE,'são negativos e',contNUL,'são nulos')

#1H)
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

#2- Implemente um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo.
#A cada tentativa errada, o programa informa se o número a adivinhar está abaixo ou acima.

import random
sorteio=random.randint(1,10)
tentativas=0
acerto=False
while acerto!=True:
    while tentativas <3 and acerto!=True:
        resposta=int(input('o computador fez um sorteio de um número de 1 a 10, qual número você acha que é? '))
        if resposta==sorteio:
            print('Você Acertou')
            acerto=True
        else:
            print('Resposta Errada!')
            tentativas=tentativas+1
            acerto=False
            if resposta < sorteio:
                print('dica: o número do sorteio é maior que a sua resposta!')
            else:
                print('dica: o número do sorteio é menor que a sua resposta!')

#3- Elabore um programa que lê um número de 1 a 9 e mostra a tabuada de multiplicação do número.
def tabuada(n):
    for i in range(1,11):
        res=n*i
        print(n,'x',i,'=',res)

continuar=True

while continuar!=False:
    escolhaT=int(input('digite o número da tabuada que deseja: '))
    print('exibindo a tabuada do número',escolhaT,'...')
    tabuada(escolhaT)
    repetir=0
    while repetir !='s' and repetir !='n':
        repetir=input('Calcular outro número (s/n)?')
        if repetir=='s':
            continuar=True
        elif repetir=='n':
            continuar=False
            print('encerrando programa...')
        else:
            print('Erro! por favor digite s ou n')
            repetir=0

#4 -Escrever um programa que calcule todos os números divisíveis por certo valor indicado pelo usuário (o
#resto da divisão por este número deve ser igual a zero), compreendidos em um intervalo também
#especificado pelo usuário. O usuário deve entrar com um primeiro valor correspondente ao divisor e
#após ele vai fornecer o valor inicial do intervalo, seguido do valor final deste intervalo.

divisor=int(input('digite o número divisor: '))
a=int(input('digite o número de inicio do intervalo: '))
b=int(input('digite o número de final do intervalo: '))
print('calculando todos os números divisíveis por',divisor,'dentro do intervalo de',a,'até',b,'...')
for divido in range(a,b+1):
    if divido%divisor==0:
        print(divido,'é divisível por',divisor)

#5 -. Para x alunos da Unisinos, ler as notas do grau A e grau B e calcular a média considerando o sistema
#de notas da Unisinos. Se o aluno estiver aprovado escrever “APROVADO”. Caso contrário, ler o grau C
#e pedir qual o grau que deve ser substituído (A ou B, maiúsculo ou minúsculo), recalcular a média. Se
#estiver aprovado, escrever “APROVADO”, caso contrário escrever “REPROVADO”. No final escrever a
#média geral dos alunos.

#funções
def mediaUni(grauA, grauB):
    media=(grauA+ 2*grauB)/3.0
    return media
def somaGeral(notaF,somageral):
    somageral=notaF+somageral
    return somageral

#variaveis
nAlunos=int(input('digite o número de alunos cujas notas serão avaliadas: '))
aluno=0
grauA=0
grauB=0
notaF=0
grauC=0
media=0
somageral=0
#main#
for aluno in range(1,nAlunos+1):
    grauA=float(input('digite a nota do grau A: '))
    grauB=float(input('digite a nota do grau B: '))
    mediaUni(grauA,grauB)
    notaF=mediaUni(grauA,grauB)
    if notaF >= 6:
        print('a média final do aluno',aluno,'foi',notaF)
        print('o aluno',aluno,'foi Aprovado!')
    elif notaF < 6:
        print('a média final do aluno',aluno,'consderando o grau A e B foi',notaF)
        print('o aluno',aluno,'ainda não foi aprovado!')
        escolhaGrau=0
        grauC=0
        notaValida=False
        while escolhaGrau !='a' and escolhaGrau !='b' or notaValida !=True:
            grauC=float(input('informe a nota do grauC: '))
            escolhaGrau=input('escolha um grau para substituir pelo grauC, (a/b): ')
            if grauC < 0 or grauC >10:
                print('Erro! por favor registre uma nota válida entre 0 a 10')
                notaValida=False
            elif escolhaGrau=='a':
                notaF=mediaUni(grauC,grauB)
                notaValida=True
            elif escolhaGrau=='b':
                notaF=mediaUni(grauA,grauC)
                notaValida=True
            else:
                print('Erro! escolha a ou b para ser substituido')
                notaValida=False
            
        if notaF >=6:
            print('a média final do aluno',aluno,'foi',notaF)
            print('o aluno',aluno,'foi Aprovado!')
        else:
            print('a média final do aluno',aluno,'foi',notaF)
            print('o aluno',aluno,'foi Reprovado!')

    somageral=somaGeral(notaF,somageral)

mediaGeral=somageral/nAlunos
print(mediaGeral,'pontos foi a média geral entre todos os',nAlunos,'alunos avaliados')

#6 -









