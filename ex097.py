# Função
def escreva(Mensagem):
    tamanho= len(Mensagem) + 4
    print('~' * tamanho)
    print(f'  {Mensagem}')
    print('~' * tamanho)


# Programa Principal
Mensagem= str(input('Escreva sua mensagem: '))
escreva(Mensagem)