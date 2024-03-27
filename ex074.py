from random import randint
numeros = (randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10),
           randint(1, 10))
menor = 10
maior = 0
print('Os valores sorteados foram :', end='')
for n in numeros:
    print(f'{n} ', end='')
    if n < menor:
        menor = n
    if n > maior:
        maior = n
print(f'\nO maior número foi o {maior}')
print(f'O menor número digitado foi {menor}')