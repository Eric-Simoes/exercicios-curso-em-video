valor = float(input('Digite o valor do produto: '))
FormaPag = str(input('Digite a forma de pagamento: '))
Parcelar = str(input('Deseja parcelar no cartão: [S/N]'))

if Parcelar == 'N':
    if FormaPag == 'dinheiro' or FormaPag == 'cheque':
        ValorFinal = valor - (valor * 0.1)
        print('O valor final foi {:.2f}R$'.format(ValorFinal))
    elif FormaPag == 'cartão':
        ValorFinal = valor - (valor * 0.05)
        print('O valor final foi {:.2f}R$'.format(ValorFinal))
else:
    vezes = int(input('Em quantas vezes deseja parcelar: '))
    if vezes <= 2:
        ValorFinal = valor
        print('O valor final foi {:.2f}R$'.format(ValorFinal))
    else:
        ValorFinal = valor + (valor * 0.2)
        print('O valor final foi {:.2f}R$'.format(ValorFinal))