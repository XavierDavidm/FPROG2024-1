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