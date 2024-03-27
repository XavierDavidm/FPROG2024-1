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
aposta=int(input('você aposta em 0 ou 1: '))
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
















