print(f'='*30)
print(f'    SUPERMERCADO JACOMAR    ')
print(f'='*30)
continuar = 'S'
total_gasto = 0
mais_1000 = 0
mais_barato = 10000
while True:
    if continuar == 'N':
        break
    print('-'*30)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    print('-'*30)
    total_gasto += preco
    if preco > 1000:
        mais_1000 += 1
    if preco < mais_barato:
        produto_mais_barato = nome
        preco_mais_barato = preco
    continuar = str(input('Deseja continuar com a compra [S/N]: '))
    if continuar != 'S' and 'N':
        continuar = str(input('Deseja continuar com a compra [S/N]: '))
print(f'O total da compra foi: {total_gasto} \n O total de produtos que custaram mais de R$ foi {mais_1000} \n O produto mais barato foi {produto_mais_barato} custando {preco_mais_barato}')

