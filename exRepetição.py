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
    





















