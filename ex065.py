continuar = 'sim'
menor = 1000
maior = 0
soma = 0
contador = 0
while continuar != 'nao':
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma = soma + numero
    contador += 1
    media = soma / contador
    continuar = str(input('Deseja continuar? '))
print(maior, menor, media, soma)