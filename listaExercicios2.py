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

#.4- Faça um algoritmo que permita ao aluno calcular a sua média final na Unisinos. Leia a nota do grau
#A e do grau B e escreva o resultado na tela. Lembrando que o Grau A vale 1/3 e o Grau B 2/3

mediaA=float(input('digite sua nota do grau A: '))
mediaB=float(input('digite sua nota do grau B: '))
mediaFinal= round(mediaA*1/3 + mediaB*2/3)
print('sua media A foi ',mediaA,'sua media B foi ',mediaB,'então sua media final é',mediaFinal)

#.5- Um motorista deseja encher o tanque do seu carro com gasolina. Escreva um algoritmo para ler o
#preço do litro da gasolina e o valor que o motorista tem disponível para abastecer. Calcule quantos
#litros ele conseguiu colocar no tanque e exiba na tela.
precoLitroGasolina=5.50
dinheiroMotorista=float(input('digite o valor disponivel: '))
totalLitros=round(dinheiroMotorista/precoLitroGasolina)
print('voce colocou',totalLitros,'Litros de gasolina no tanque')





















