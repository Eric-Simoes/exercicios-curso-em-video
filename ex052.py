numero = int(input('digite um número: '))
primo = 0
for contador in range(1, numero+1):
    if numero % contador == 0:
        primo = primo + 1
if primo == 2:
    print('O número digitado {} é primo!'.format(numero))
else:
    print('O número digitado {} não é primo!'.format(numero))
