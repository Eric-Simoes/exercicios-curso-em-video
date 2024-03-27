numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os seguintes números{numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('Os números pares que foram digitados são: ')
for contador in numeros:
    if contador % 2 == 0:
        print(contador)
