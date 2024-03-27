from random import randint
from time import sleep
# Função
def pontinhos_guanabara():
    print('-='*30)
def mensagem():
    porcentagem= []
    print('Analisando valores passados... ')


# Programa Principal

for quantidade_valores in range(6, 0, -1):
    numeros = []
    for indice in range(0, quantidade_valores):
        valor = randint(0, 10)
        if indice == 0:
            maior_numero = valor
        else:
            if maior_numero < valor:
                maior_numero = valor
        numeros.append(valor)
    pontinhos_guanabara()
    mensagem()
    print(f'{numeros} Foram informados {len(numeros)} valores ao todo.'
          f'\nO maior valor informado foi {maior_numero}')
