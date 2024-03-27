numeros = [[], []]

for contador in range(1, 8):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros.sort
print(f'Foram digitados {numeros[1]} ímpares! \nForam digitados {numeros[0]} pares!')