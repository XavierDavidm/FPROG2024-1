divisor=int(input('digite o número divisor: '))
a=int(input('digite o número de inicio do intervalo: '))
b=int(input('digite o número de final do intervalo: '))
print('calculando todos os números divisíveis por',divisor,'dentro do intervalo de',a,'até',b)
for divido in range(a,b+1):
    if divido%divisor==0:
        print(divido,'é divisivél por',divisor)