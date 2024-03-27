idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('Ainda não está na hora de você se alistar!')
elif idade == 18:
    print('Está na hora de você se alistar!')
else:
    print('Já passou o tempo de você se alistar!')