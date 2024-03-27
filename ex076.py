listagem = ('Laranja', 1.75, 'Chocolate', 8.89, 'Costela', 27.99, 'Milka', 14.67, 'Peixe', 45.50)
print('=' * 38)
print(f'{"JACOMAR":^38}')
print('=' * 38)
print('*' * 38)
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(f'{listagem[produto]:.<30}', end='')
    else:
        print(f'R${listagem[produto]:>6.2f}')
print('*' * 38)