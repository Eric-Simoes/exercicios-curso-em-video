s = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s = s + num
print('O resultado da soma dos números pares foi de {}'.format(s))
