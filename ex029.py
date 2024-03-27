vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Sua multa foi de {} reais!'.format(multa))
