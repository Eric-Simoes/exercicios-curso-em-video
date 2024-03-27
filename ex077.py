palavras = ('Estudar', 'Trabalhar', 'Montanha', 'Traduzir')
print('-'*50)
print(f'{"CONTANDO AS VOGAIS":^50}')
print('-'*50)
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')