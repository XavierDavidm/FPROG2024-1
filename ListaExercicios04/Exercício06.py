#lista 04 while e for

#6 -Crie um algoritmo que sorteie 5 valores entre 0 e 100 e depois imprima o menor, o maior e a média
#dos valores sorteados.

#area import
import random

#area function

#area variaveis
n1=0
n2=0
n3=0
n4=0
n5=0

#MAIN#
n1=random.randint(0,100)
n2=random.randint(0,100)
n3=random.randint(0,100)
n4=random.randint(0,100)
n5=random.randint(0,100)

print(n1,n2,n3,n4,n5)
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print(n1,'é o maior numero sorteado')
elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print(n2,'é o maior numero sorteado')
elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print(n3,'é o maior numero sorteado')
elif n4>n1 and n4>n3 and n4>n2 and n4>n5:
    print(n4,'é o maior numero sorteado')
elif n5>n1 and n5>n3 and n5>n4 and n5>n2:
    print(n5,'é o maior numero sorteado')

if n1<n2 and n1<n3 and n1<n4 and n1<n5:
    print(n1,'é o menor numero sorteado')
elif n2<n1 and n2<n3 and n2<n4 and n2<n5:
    print(n2,'é o menor numero sorteado')
elif n3<n1 and n3<n2 and n3<n4 and n3<n5:
    print(n3,'é o menor numero sorteado')
elif n4<n1 and n4<n3 and n4<n2 and n4<n5:
    print(n4,'é o menor numero sorteado')
elif n5<n1 and n5<n3 and n5<n4 and n5<n2:
    print(n5,'é o menor numero sorteado')
    
media=(n1+n2+n3+n4+n5)/5
print('a média entre todos os números sorteados é:',media)