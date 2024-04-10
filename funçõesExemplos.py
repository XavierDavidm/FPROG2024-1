#introduçao funções 
#funçoes sao usadas para repetir linhas de codigo e executar comandos usando variveis diferentes
#reaproveitamento de codigos
#Criaçao de bibliotecas de codigo fonte para reutilizar funções
#exemplo import random
#linguagens não python possuem um codigo main/entry point usando '_main_' ou 'main' para indicar a linha de codigo principal
#para escrever função:
# def nomeDaFunção (lista de parametros):
# -------bloco de codigo normal(if,while,for,variaveis)
# + return as vezes
#normalmente nomes de ações e verbos como nome de função para indicar seu proposito(se muito grande usar palavras chave)
#BOAS PRATICAS===usar a area inicial do codigo para as funções e depois começar o programa principal
#pois as funções não funcionam se forem posicionadas depois de serem chamadas sempre colocalas antes do codigo

#ex1
#area import#

#area funções#
def minhaPrimeiraFuncao():
    print('olá função!')

def funParametros(p1,p2,p3):
    print('olá parametros!')
    print('parametro 1:',p1)
    print('parametro 2:',p2)
    print('parametro 3:',p3)

#####programa principal#####
print('teste')
#chamando a função=== nomedafunção()
minhaPrimeiraFuncao()

#parametros da funçao vem dentro (parametro1,parametro2,...)
#no python os parametros se adaptam a qualquer tipo de variavel, em outras liguagens é nescessario especificar int,float,string
#int
funParametros(1,2,3) 
#float
funParametros(1.1,2.2,3.3)
#string
funParametros('A','B','C')
#bol
funParametros(False,True,False)
#podem ser mistos os parametros/lembrando que em outras linguagens tem que especificar a tipagem,
# ex funçao(int p1,float p2,string p3)























