# Função
def Info_Jogador(nome='Desconhecido', gols=0):
    if nome != 'Desconhecido':
        return f'O jogador {nome} fez {gols} gol(s).'

# Programa principal
nome= str(input('Digite o nome do jogador: '))
gols= int(input('Quantos gols o jogador fez: '))
print(Info_Jogador(nome, gols))