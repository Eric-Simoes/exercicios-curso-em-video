s = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    s += numero
print(f'A soma dos numeros foi {s}')