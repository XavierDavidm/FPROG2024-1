#.1- Faça um algoritmo que leia uma quantidade de tempo em minutos e escreva o tempo equivalente 
#em segundos na tela.
#float(numeros reais) e int(numeros inteiros) convertem o input para valores logicos possibilitando contas
minutos = float(input('quantos minutos?'))
segundos = minutos*60
print(minutos, 'minutos equivalem','a',segundos,'segundos')

#.2- Um turista deseja comprar dólares em uma casa de câmbio. Escreva um programa que leia a 
#cotação do dólar para real, a quantidade de dólares que o turista deseja comprar, e calcule o valor 
#total em reais que ele precisará pagar.

dolarcotacao=4.97 
print('a atual cotação do dolar para real é',dolarcotacao)
quantidade = float(input('quantos dolares deseja comprar?'))
total=dolarcotacao*quantidade
print('voce precisa pagar',total,'reais para ter',quantidade,'dolares!')

#.3- Um restaurante de buffet a quilo cobra R$ 40,00 por quilo. Escreva um programa que leia o peso 
#do prato do cliente e calcule o valor a ser pago.

porquilo=40.00
peso=float(input('informe o peso do prato: '))
valorbuffet=peso*porquilo
print('voce devera pagar',valorbuffet,'reais por',peso,'quilos de comida')

























