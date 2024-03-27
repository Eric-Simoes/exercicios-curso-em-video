valor = []
menor = 0
maior = 0
for contador in range(0,5):
    valor.append(int(input(f'Digite um valor para a posição {contador}: ')))
    if contador == 0:
        maior = menor = valor[contador]
    else:
        if valor[contador] < menor:
            menor = valor[contador]
        if valor[contador] > maior:
            maior = valor[contador]
print('*'*30)
print(f'Você digitou os seguintes valores {valor}')
print(f'O menor valor digitado foi o {menor} na posição', end='')
for indice, numero in enumerate(valor):
    if numero == menor:
        print(f' {indice}...', end='')
print(f'\nO maior valor digitado foi o {maior} na posição', end='')
for indice, numero in enumerate(valor):
    if numero == maior:
        print(f' {indice}... ', end='')
