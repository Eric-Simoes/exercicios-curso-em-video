ano = int(input('Digite o ano: '))
if (ano % 4 == 0) and (ano % 100 != 0):
    print("O ano digitado {} é bissexto!".format(ano))
else:
    print('O ano digitado {} não é bissexto!'.format(ano))
