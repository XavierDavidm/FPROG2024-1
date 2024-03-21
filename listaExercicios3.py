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












