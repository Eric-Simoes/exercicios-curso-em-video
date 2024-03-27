sal = float(input('Digite o seu salário: '))
if sal > 1250.00:
    aum = sal * 0.10
    print('Você terá um aumento de {:.2f} R$'.format(aum))
else:
    aum = sal * 0.15
    print('Você terá um aumento de {:.2f} R$'.format(aum))

