Cadastro_do_Jogador= {}
Time = []
Numero_de_Gols= []
Total_de_Gols= 0
contador = 0
Codigo= []
while True:
    Cadastro_do_Jogador.clear()
    Numero_de_Gols.clear()
    Cadastro_do_Jogador['nome']= str(input('Nome do jogador: '))
    Cadastro_do_Jogador['partidas']= int(input('Número de partidas jogadas: '))
    for Contador in range(1, Cadastro_do_Jogador['partidas']+1):
        Gols = (int(input(f'Quantos gols foram marcados na partida {Contador}:  ')))
        Total_de_Gols += Gols
        Numero_de_Gols.append(Gols)
    Cadastro_do_Jogador['gols'] = Numero_de_Gols[:]
    Cadastro_do_Jogador["total"]= Total_de_Gols
    Time.append(Cadastro_do_Jogador.copy())
    while True:
        Continuar = str(input('Deseja continuar [S/N]: ')).upper()
        if Continuar in 'SN':
            break
        else:
            print('ERRO! Digite novamente!')
    if Continuar == 'N':
        break
print('-='*40)
print('cod ',end='')
for i in Cadastro_do_Jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(Time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    Mostrar_Dados_Jogador= int(input('Digite o Código do jogador desejado (999 para parar): '))
    if Mostrar_Dados_Jogador == 999:
        break
    if Mostrar_Dados_Jogador >= len(Time):
        print(f'ERRO! Não existe jogador com o código {Mostrar_Dados_Jogador}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {Time[Mostrar_Dados_Jogador]["nome"]}:')
        for contador in range(0, Time[Mostrar_Dados_Jogador]["partidas"]):
            print(f'No jogo {contador} fez {Time[Mostrar_Dados_Jogador]["gols"][contador]}.')
    print('--'*30)