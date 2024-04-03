etiqueta=-1
while etiqueta < 0:
    etiqueta=float(input('digite o valor da etiqueta do produto: '))
    if etiqueta < 0:
        print('valor do produto inválido, por favor registre o valor correto')
formaDePagamento=-1
while formaDePagamento!='dinheiro' and formaDePagamento!='cartão' and formaDePagamento!='cartão2x' and formaDePagamento!='cartão3x':
    print('À vista em dinheiro(15% de desconto)',          '(dinheiro)') 
    print('À vista no cartão de crédito(10% de desconto)', '(cartão)')
    print('Em duas vezes(sem juros)',                      '(cartão2x)')
    print('Em três vezes(juros de 10%)',                   '(cartão3x)')
    formaDePagamento=input('digite a forma de pagamento que deseja (por favor digite a opção entre parenteses): ')
    if formaDePagamento=='dinheiro':
        totalfinalproduto=etiqueta*0.85
        print('você pagou em dinheiro à vista',totalfinalproduto,'reais')
    elif formaDePagamento=='cartão':
        totalfinalproduto=etiqueta*0.90
        print('você pagou no cartão à vista',totalfinalproduto,'reais')
    elif formaDePagamento=='cartão2x':
        totalfinalproduto=etiqueta
        print('você pagou no cartão em duas vezes',totalfinalproduto,'reais')     
    elif formaDePagamento=='cartão3x':
        totalfinalproduto=etiqueta*1.10
        print('você pagou no cartão em tres vezes',totalfinalproduto,'reais')
    else:
        print('forma de pagamento inválida, por favor insira novamente a forma de pagamento que deseja de acordo com a tabela a seguir')

                