homem_velho = 'a'
mais_velho = 0
mulheres_menos_20 = 0
total_idades = 0
media_idades = 0
for contador in range(1,5):
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))
    if sexo == 'M':
        if idade > mais_velho:
            homem_velho = nome
            mais_velho = idade
    if sexo == 'F':
        if idade < 20:
            mulheres_menos_20 = mulheres_menos_20 + 1
    total_idades = total_idades + idade
media_idades = total_idades / 4
print('O homem mais velho foi o {} com {} anos'.format(homem_velho, mais_velho))
print('O total de mulheres com menos de 20 anos foi {}'.format(mulheres_menos_20))
print('A média de idades foi {}'.format(media_idades))