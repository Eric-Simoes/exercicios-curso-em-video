pessoa = []
galera = []
maior_peso = menor_peso = 0
while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(int(input('Digite o seu peso: ')))
    if len(galera) == 0:
        maior_peso = menor_peso = pessoa[1]
        nome_maior_peso = nome_menor_peso = pessoa[0]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
            nome_maior_peso = pessoa[0]
        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]
            nome_menor_peso = pessoa[0]
    galera.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar not in 'SsNn':
        continuar = str(input('Opção diferente de [S/N], digite novamente: '))
    if continuar in 'Nn':
        break
print('***' * 20)
print(f'Foram cadastras {len(galera)} de pessoas ao todo')
print(f'O maior peso registrado foi o {maior_peso} Kg da pessoa {nome_maior_peso}')
print(f'O menor peso registrado foi o {menor_peso} Kg da pessoa {nome_menor_peso}')