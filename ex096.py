# Função
def area(Largura, Comprimento):
    Resultado= Largura * Comprimento
    print(f'\nA area do terreno {Largura}x{Comprimento} é de {Resultado}m²')


# Programa principal
print(f'{"Controle de Terreno":^30}')
print('-'*30)
Largura= float(input('Largura (m): '))
Comprimento= float(input('Comprimento (m): '))
area(Largura, Comprimento)


