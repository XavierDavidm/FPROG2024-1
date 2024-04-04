resposta=1
while resposta != 'S' and resposta != 'N':
    resposta=input('responda sim(S) ou não(N)')
    if resposta == 'S':
        print('voce respodendeu sim')
    elif resposta == 'N':
        print('você respondeu não')
    else:
        print('resposta invalida')

#enquanto o user não digitar S ou N o programa repete a pergunta usando a condição while
   
#contador com while: escrever o nome 10 vezes
nome=input('digite seu nome: ')
#variavel para contar quantidade de vezes que o nome foi escrito 
cont=0
while cont<10:
    print(nome)
    cont=cont+1 #incremento em 1 unidade

#Faça um programa que permita o usuário
#entrar com uma senha no máximo em 3
#tentativas
#– Quais são as condições para a repetição?
#• Quando a repetição deve parar?
senhaCadastrada=123
senha=-10
tentativas=0
while senhaCadastrada != senha and tentativas <=3:
    senha=int(input('digite sua senha: '))
    if senhaCadastrada == senha:
        print('olá sua senha esta correta!')
    elif tentativas >=2:
        print('você digitou a senha incorreta 3 vezes, aguarde 1h para tentar novamente')
        tentativas=4
    else:
        print('senha invalida tente novamente!')
        tentativas = tentativas + 1

# modelo simples sem print da quantidade de tentativas restantes


#comando for (VARIAVEL) in range
counter=0
for counter in range(10):
    print(counter)





















