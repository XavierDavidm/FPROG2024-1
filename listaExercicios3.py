#.1-Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for
#diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.
numero1=float(input('digite um numero: '))
numero2=float(input('digite um numero: '))
if numero2 != 0:
    total=numero1/numero2
    print(total)
else: 
    print('erro! o numero 0 não é valido para divisão')

#.2- Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A
#+ C.
A=float(input('digite o valor de A: '))
B=float(input('digite o valor de B: '))
C=float(input('digite o valor de C: '))
if A+B<A+C:
    print('A+B é menor que A+C')
else:
    print('A+B é maior que A+C')

#.3- Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo
#o resultado
numero=float(input('digite um numero positivo ou negativo: '))
if numero >0:
    final=numero*2
    print('o dobro de',numero,'é',final)
else:
    final=numero*3
    print('o triplo de',numero,'é',final)

#.4- Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3.
numerodivisivel=int(input('informe um numero para verificar se é divisivel por 3: '))
if numerodivisivel%3==0:
    print(numerodivisivel,'é divisivel por 3')
else:
    print(numerodivisivel,'não é divisivel por 3')

#.5- Faça um algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se
#é ímpar
num=int(input('digite um numero par ou impar: '))
if num%2==0:
    print(num,'é par')
else:
    print(num,'é impar')

#.6- Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
#disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
#um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
#soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
#que o programa venceu
import random
aposta=int(input('você, aposta em 0 ou 1: '))
numDoUser=int(input('digite um numero de 0 a 5: '))
sorteio=random.randint(0,5)
print('o computador jogou',sorteio)
print('você jogou',numDoUser)
resultadoDaAposta=sorteio+numDoUser
if resultadoDaAposta%aposta==0:
    print('você ganhou')
else:
    print('você perdeu')

#.7- Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa
#deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto
#segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é
#318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.
salario=float(input('informe seu salário: '))
taxaDeDesconto= 0.11
salDesc=salario*taxaDeDesconto
if salDesc > 318.20:
    descontoPrevidencia=318.20
else:
    descontoPrevidencia=salDesc
print('para um salario de',salario,'reais é aplicado',descontoPrevidencia,'reais para o desconto previdenciário')

#.8- Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor
#da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço
#for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na
#tela o valor de venda.
produto=float(input('digite o valor do produto que deseja vender: '))
if produto < 20.00:
    taxaLucro=produto*0.45
elif produto <= 50:
    taxaLucro=produto*0.35
else:
    taxaLucro=produto*0.25
precofinal=produto+taxaLucro
print('o produto deve ser vendido por',precofinal,'reais')

#.9-Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação
#de cada moeda em relação ao real. Depois apresente o seguinte menu:
#1) Converter de Real para Euro
#2) Converter de Real para Dólar
#3) Converter de Euro para Dólar
#4) Converter de Euro para Real
#5) Converter de Dólar para Euro
#6) Converter de Dólar para Real
#Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda
#destino.
dolar=float(input('informe a cotação atual do dolar para real: '))
euro=float(input('informe a cotação atual do euro para real: '))
print('1) Converter de Real para Euro')
print('2) Converter de Real para Dólar')
print('3) Converter de Euro para Dólar')
print('4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro')
print('6) Converter de Dólar para Real')
conversaoEscolhida=0
while conversaoEscolhida !=(1,2,3,4,5,6):
    conversaoEscolhida=int(input('digite o número da conversão que deseja realizar: '))
    quantidadeMoeda=float(input('digite a quantidade da moeda origem que deseja converter: '))
    CRE=quantidadeMoeda/euro
    CRD=quantidadeMoeda/dolar
    CED=(quantidadeMoeda*euro)/dolar
    CER=quantidadeMoeda/euro
    CDE=(quantidadeMoeda*dolar)/euro
    CDR=quantidadeMoeda*dolar
    if conversaoEscolhida==1:
        print(quantidadeMoeda,'Reais são',CRE,'Euros')
    elif conversaoEscolhida==2:
        print(quantidadeMoeda,'Reais são',CRD,'Dólares')
    elif conversaoEscolhida==3:
        print(quantidadeMoeda,'Euros são',CED,'Dólares')
    elif conversaoEscolhida==4:
        print(quantidadeMoeda,'Euros são',CER,'Reais')
    elif conversaoEscolhida==5:
        print(quantidadeMoeda,'Dólares são',CDE,'Euros')
    elif conversaoEscolhida==6:
        print(quantidadeMoeda,'Dólares são',CDR,'Reais')
    else:
        print('o numero da conversão escolhida não é valido, digite um dos numeros da tabela')

#.10- Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que
#simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no
#começo do programa quantas faces quer, para depois fazer o sorteio.
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

#.11- Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de
#cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50,
#R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao
#solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram
#exibidas informações sobre as demais cédulas):
#1 nota(s) de R$ 10.
#1 nota(s) de R$ 5.
#3 nota(s) de R$ 1.
totalNotasUser=int(input('informe a quantia que deseja trasformar em cédulas: '))
notas100=0
notas50=0
notas20=0
notas10=0
notas5=0
notas1=0
while totalNotasUser>=100:
    totalNotasUser=totalNotasUser-100
    notas100=notas100+1
while totalNotasUser>=50:
    totalNotasUser=totalNotasUser-50
    notas50=notas50+1
while totalNotasUser>=20:
    totalNotasUser=totalNotasUser-20
    notas20=notas20+1
while totalNotasUser>=10:
    totalNotasUser=totalNotasUser-10
    notas10=notas10+1
while totalNotasUser>=5:
    totalNotasUser=totalNotasUser-5
    notas5=notas5+1
while totalNotasUser>=1:
    totalNotasUser=totalNotasUser-1
    notas1=notas1+1
if notas100 > 0:
    print(notas100,'nota(s) de R$ 100')
if notas50 > 0:
    print(notas50,'nota(s) de R$ 50')
if notas20 > 0:
    print(notas20,'nota(s) de R$ 20')
if notas10 > 0:
    print(notas10,'nota(s) de R$ 10')
if notas5 > 0:
    print(notas5,'nota(s) de R$ 5')
if notas1 > 0:
    print(notas1,'nota(s) de R$ 1')
if notas1==0 and notas5==0 and notas10==0 and notas20==0 and notas50==0 and notas100==0:
    print('você não digitou um valor valido para converter em cédulas')

#.12-u







