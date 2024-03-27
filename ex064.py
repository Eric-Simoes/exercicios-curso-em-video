numero = 0
soma = 0
contador = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        soma = soma + numero
        contador = contador + 1
    else:
        soma = soma + (999 - 999)
print('soma {} contador {}'.format(soma, contador))