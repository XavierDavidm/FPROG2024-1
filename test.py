dependente=0                                          
totalplano=300+dependente
temdependente=-1
while temdependente !='S' and temdependente !='N':
        temdependente=input('você possui dependente(s) (S) ou (N): ')
        if temdependente == 'N':
            totalplano=300
            print('o total do seu plano é',totalplano)
        elif temdependente == 'S':
            idadeDependente=-1
            while idadeDependente < 0:
                totalplano=300+dependente
                idadeDependente=int(input('coloque a idade do dependente: '))  
                if idadeDependente < 0:
                    print('idade inválida, por favor coloque uma idade válida')
                elif idadeDependente <= 10:
                    dependente=100
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                elif idadeDependente > 10 and idadeDependente <= 30:
                    dependente=220
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                elif idadeDependente >= 31 and idadeDependente <= 60:
                    dependente=395
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                elif idadeDependente > 60:
                    dependente=480
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                elif idadeDependente < 0:
                    print('idade inválida, por favor coloque uma idade válida')
                
        else:
            print('resposta inválida, por favor responda se possui ou não dependentes usando (S) ou (N)')

                