#Somar os números pares
#Somar os valores da terceira coluna
#Mostrar o maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_dos_pares = soma_terceira_coluna = maior_numero_segunda_linha = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número para posição [{linha, coluna}]: '))
        if matriz[linha][coluna] % 1 == 0:
            soma_dos_pares += matriz[linha][coluna]
        if linha == 2:
            if matriz[linha][coluna] > maior_numero_segunda_linha:
                maior_numero_segunda_linha = matriz[linha][coluna]
            if coluna == 2:
                soma_terceira_coluna += matriz[linha][coluna]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos números pares foi {soma_dos_pares}')
print(f'O maior número na segunda linha é {maior_numero_segunda_linha}')
print(f'A soma dos valores presentes na terceira coluna foi {soma_terceira_coluna}')