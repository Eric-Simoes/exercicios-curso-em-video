numeros = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar == 'n':
        break
numeros.sort()
print(f'Foram digitados os seguintes valores {numeros}')