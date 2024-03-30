notaGA=-1
notaGB=-1
while notaGA < 0 or notaGB <0 or notaGA > 10 or notaGB > 10:
    notaGA=float(input('digite sua nota do grau A: '))
    notaGB=float(input('digite sua nota do grau B: '))
    mediaF=round(notaGA*1/3 + notaGB*2/3)
    if notaGA < 0 or notaGB < 0 or notaGA > 10 or notaGB > 10:
        print('nota invalida!, por favor informe uma nota de 0 a 10')
    elif mediaF >=6:
        print('sua média final foi',mediaF)
        print('você foi aprovado, parabéns!')
    else:
        print('sua média final foi',mediaF)
        print('Você não foi aprovado, deverá realizar a recuperação(grau C)')
        notaGC=-1
        while notaGC < 0 or notaGC >10:
            notaGC=float(input('digite sua nota do grau C (recuperação): '))
            if notaGC < 0 or notaGC >10:
                print('nota invalida!, por favor informe uma nota de 0 a 10')
            else:
                escolharec=1
                while escolharec !='a' and escolharec !='b':
                    escolharec=input('escolha qual grau deseja substuir (a) ou (b): ')
                    if escolharec !='a' and escolharec!='b':
                        escolharec=1
                        print('por favor escolha qual grau será substituido (a) ou (b)')
                    else:
                        if escolharec =='a':
                            mediaF=round(notaGC*1/3 + notaGB*2/3)
                            escolharec='a'
                            if mediaF >= 6:
                                print('você foi aprovado com',mediaF,'média parabéns!')
                            else:
                                print('sua média final foi',mediaF)
                                print('você foi reprovado mesmo com o grau C')
                        elif escolharec =='b':
                            mediaF=round(notaGA*1/3 + notaGC*2/3)
                            escolharec='b'
                            if mediaF >= 6:
                                print('você foi aprovado com',mediaF,'média parabéns!')
                            else:
                                print('sua média final foi',mediaF)
                                print('você foi reprovado mesmo com o grau C')

                