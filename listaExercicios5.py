#1- leia o nome do usario e criar uma função para cumprimentar o usuario usando seu nome

def cumprimentar(nome):
    print('Olá, seja bem vindo',nome,'!')
#as variaveis não precisam ser o mesmo nome do parametro da função
nome1=input('usuario1, digite seu nome: ')
cumprimentar(nome1)

nome2=input('usuario2, digite seu nome: ')
cumprimentar(nome2)

#usando for
for i in range(5):
    print('usuario', i+1, end='')
    nome= input(", digite seu nome: ")
    cumprimentar(nome)

#2- tabuada

#area funçao#
def tabuada(n):
    for i in range(1,11):
        res=n*i
        print(n,'x',i,'=',res)

#main#
n=int(input('digite um número para saber a tabuada dele: '))
tabuada(n)

#3- 
























