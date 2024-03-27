continuar = 'S'
menos_18 = 0
homem= 0
mulher_menos_20 = 0
while True:
    if continuar == 'N':
        break
    nome = str(input('Digite um nome: '))
    sexo= str(input('Digite o sexo [M/F]: '.upper()))
    idade = int(input('Digite a idade: '))
    if idade < 19:
        menos_18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 21:
        mulher_menos_20 += 1
    continuar = str(input('Deseja continuar[S,N]: '.upper()))
print(f'Foram inseridos um total de {menos_18} pessos com menos de 18 anos. \n Foram inseridos um todal de {homem} homens. \n Foram inseridos um todas de {mulher_menos_20} com menos de 18.')