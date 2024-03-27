sexo = 'a'
while (sexo != 'M') and (sexo != 'F'):
    sexo = str(input('Digite o sexo [M/F]: '))
    if (sexo != 'M') and (sexo != 'F'):
        print('Opção inválida')
print('O sexo digitado foi {}!'.format(sexo))
print('Fim do programa!')