maior_peso = 0
nome_maior_peso = 'a'
menor_peso = 1000
nome_menor_peso = 'a'
for contador in range(1, 3):
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso:'))
    if peso > maior_peso:
        maior_peso = peso
        nome_maior_peso = nome
    if peso < menor_peso:
        menor_peso = peso
        nome_menor_peso = nome
print('O maior peso foi do {} com {}kg'.format(nome_maior_peso, maior_peso))
print('O menor peso foi do {} com {}kg'.format(nome_menor_peso, menor_peso))