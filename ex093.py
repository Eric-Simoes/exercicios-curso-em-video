Cadastro_Jogador = {}
Numero_de_Gols= []
Total_de_Gols= 0
Cadastro_Jogador['Nome']= str(input('Nome do jogador: '))
Cadastro_Jogador['Numero_Partidas']= int(input('Número de partidas jogadas: '))
for Contador in range(1, Cadastro_Jogador['Numero_Partidas']+1):
    Numero_de_Gols.append(int(input(f'Quantos gols foram marcados na partida {Contador}:  ')))
Cadastro_Jogador['Numero_de_Gols']= Numero_de_Gols[:]
print('-='*30)
print(Cadastro_Jogador)
print('-='*30)
for k, v in Cadastro_Jogador.items():
    print(f'O campo "{k}" tem o valor {v}')
print('-='*30)
print(f'- o jogador {Cadastro_Jogador["Nome"]}')
print(f'- jogou {Cadastro_Jogador["Numero_Partidas"]} partidas')
for Contador in range(0, Cadastro_Jogador['Numero_Partidas']):
    print(f'=> na parida {Contador+1} marcou {Numero_de_Gols[Contador]}.')
    Total_de_Gols += Numero_de_Gols[Contador]
print(f'Foi um total de {Total_de_Gols} gols.')
print('-='*30)