dolar=float(input('informe a cotação atual do dolar para real: '))
euro=float(input('informe a cotação atual do euro para real: '))

print('1) Converter de Real para Euro')
print('2) Converter de Real para Dólar')
print('3) Converter de Euro para Dólar')
print('4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro')
print('6) Converter de Dólar para Real')
conversaoEscolhida=0
while conversaoEscolhida !=(1,2,3,4,5,6):
    conversaoEscolhida=int(input('digite o numero da conversão que deseja realizar: '))
    quantidadeMoeda=float(input('digite a quantidade da moeda origem que deseja converter: '))
    CRE=quantidadeMoeda/euro
    CRD=quantidadeMoeda/dolar
    CED=(quantidadeMoeda*euro)/dolar
    CER=quantidadeMoeda/euro
    CDE=(quantidadeMoeda*dolar)/euro
    CDR=quantidadeMoeda*dolar
    if conversaoEscolhida==1:
        print(quantidadeMoeda,'Reais são',CRE,'Euros')
    elif conversaoEscolhida==2:
        print(quantidadeMoeda,'Reais são',CRD,'Dólares')
    elif conversaoEscolhida==3:
        print(quantidadeMoeda,'Euros são',CED,'Dólares')
    elif conversaoEscolhida==4:
        print(quantidadeMoeda,'Euros são',CER,'Reais')
    elif conversaoEscolhida==5:
        print(quantidadeMoeda,'Dólares são',CDE,'Euros')
    elif conversaoEscolhida==6:
        print(quantidadeMoeda,'Dólares são',CDR,'Reais')
    else:
        print('o numero da conversão escolhida não é valido, digite um dos numeros da tabela')