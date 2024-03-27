num = int(input('Digite um número: '))
print('''Escolha uma das opções abaixo
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)))
else:
    print('Opção inválida!')