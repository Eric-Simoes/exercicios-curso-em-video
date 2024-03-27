# Funão
def Voto(Ano_de_Nascimento):
    if (2024 - Ano_de_Nascimento) < 18:
        return f'Inapto(a) para votar'
    if (2024 - Ano_de_Nascimento) > 18:
        return f'Apto(a) para votar'

# Programa Principal
Ano_de_Nascimento= int(input('Informe seu ano de nascimento: '))
print(Voto(Ano_de_Nascimento))