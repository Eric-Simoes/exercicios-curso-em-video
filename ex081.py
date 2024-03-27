numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar not in 'SsNn':
        print('Digite uma opção válida')
        continuar = str(input('Deseja continuar [S/N]: '))
    if continuar in 'Nn':
        break
print('*' * 30)
print(f'Foram digitados {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os seguinte números foram inseridos com sucesso na lista {numeros}')
if 5 in numeros:
    print('O número 5 está inserido na lista')
else:
    print('O número 5 não está presente na lista')
print('*** Fim do Programa ***')
