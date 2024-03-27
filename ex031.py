D = int(input('Digite a distância de sua viagem: '))
if D < 200:
    custo = D * 0.5
    print('O custo de sua viagem ficou em {:.2f} R$'.format(custo))
else:
    custo = D * 0.45
    print('O custo de sua viagem ficou em {:.2f} reais'.format(custo))

