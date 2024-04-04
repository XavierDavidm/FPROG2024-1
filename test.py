senhaCadastrada=123
senha=-10
tentativas=0
check=True
tentativasR=3
while senhaCadastrada != senha and check!=True:
    senha=int(input('digite sua senha: '))
    if senhaCadastrada == senha:
        print('olá sua senha esta correta!')
        check=True
    elif tentativas >3:
        print('você digitou a senha incorreta 3 vezes, aguarde 1h para tentar novamente')
        check=True
    else:
        print('senha invalida tente novamente!')
        tentativas = tentativas + 1
        tentativasR=tentativasR-tentativas
        print(tentativasR,'restantes')
        check=False