from time import sleep
Pessoa = {}
Pessoas = []
Total_de_Pessoas = Total_de_Mulheres = Soma_das_Idades = Pessoas_acimamMedia_idades = Media_das_idades = 0
while True:
    Pessoa['Nome']= str(input('Nome: '))
    Sexo= str(input('Sexo: [M/F] ')).upper()
    if Sexo in 'MmFf':
        Pessoa['Sexo']= Sexo
    else:
        while Sexo not in 'MmFf':
            print('Digite apenas [M/F]')
            Sexo = str(input('Sexo: ')).upper()
    if Sexo in 'F':
        Total_de_Mulheres += 1
    Pessoa['Sexo']= Sexo
    Pessoa['Idade']= int(input('Idade: '))
    Soma_das_Idades += Pessoa['Idade']
    Pessoas.append(Pessoa.copy())
    Total_de_Pessoas += 1
    Continuar= str(input('Deseja continuar, apenas [S/N]: ')).upper()
    while Continuar not in 'SN':
        print('ERRO!')
        Continuar= str(input('Digite apenas [S/N]: ')).upper()
    if Continuar == 'N':
        break
    Media_das_idades = Soma_das_Idades / len(Pessoas)

print(Pessoa)
print(Pessoas)
print(Total_de_Mulheres)
print(Total_de_Pessoas)
print(Media_das_idades)
print(f'A) Ao todo foram {len(Pessoas)} cadastradas.')
print(f'B) A média de idades é {Media_das_idades:2} anos.')
print(f'C) As mulheres cadastradas foram', end='')
for pessoa in Pessoas:
    if pessoa['Sexo'] in 'F':
        print(f' {pessoa["Nome"]}', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
for pessoa in Pessoas:
    if pessoa['Idade'] > Media_das_idades:
            print(f'Nome = {pessoa["Nome"]:^10}: sexo = {pessoa["Sexo"]:^10}: idade = {pessoa["Idade"]} anos')
