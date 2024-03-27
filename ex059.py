n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

escolha = 6

while escolha != 5:
    print('[1] para somar')
    print('[2] para multiplicar')
    print('[3] para saber qual o maior número')
    print('[4] para digitar novos números')
    print('[5] para finalizar o programa')
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma dos números resultou em {}'.format(soma))
    elif escolha == 2:
        multiplicador = n1 * n2
        print('O resultado da multiplicação destes números foi {}'.format(multiplicador))
    elif escolha == 3:
        if n1 > n2:
            print('O primeiro número é maior!')
        elif n2 > n1:
            print('O segundo número é o maior!')
        else:
            print('Os números são iguais!')
    elif escolha == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    else:
        print('Opção inválida!')
print('Fim do programa!')
