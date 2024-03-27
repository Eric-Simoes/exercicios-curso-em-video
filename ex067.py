numero = 0
while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    for contador in range(1,11):
        tabuada = numero * contador
        print(f'{numero} x {contador} = {tabuada}')
