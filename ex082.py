total_numeros = []
numeros_pares = []
numeros_impares = []
while True:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    total_numeros.append(numero)
    continuar= str(input('Deseja continuar[S/N]: '))
    if continuar not in 'SsNn':
        print('Digite uma opção válida')
        continuar = str(input('Deseja continuar[S/N]: '))
    if continuar in 'Nn':
        break
print(f'{"*" * 29}')
print(f'A lista completa dos números digitados é {total_numeros}')
print(f'A lista de números pares é {numeros_pares}')
print(f'A lista de ímpares é {numeros_impares}')
print(f'{"****** FIM DO PROGRAMA ******":^30}')