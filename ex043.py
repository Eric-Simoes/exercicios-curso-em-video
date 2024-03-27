alt = float(input('Digite a altura: '))
peso = float(input('digite seu peso: '))

imc = peso / (alt * alt)

if imc < 18:
    print('Abaixo do peso!')
elif (imc > 18) and (imc <= 25):
    print('Peso ideal!')
elif (imc > 25) and (imc <= 30):
    print('Sobrepeso')
elif (imc > 30) and (imc <= 35):
    print('Obesidade')
else:
    print('Obesidade morbida')