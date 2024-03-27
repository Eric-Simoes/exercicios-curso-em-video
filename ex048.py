r = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            r = r + c
print('A soma de todos os números ímpares que se encontram no intervalo de 1 a 500 de {}'.format(r))

