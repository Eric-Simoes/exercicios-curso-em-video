from time import sleep

#Função
def borda():
    print('-='*15)
def Contagem(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    for contador in range(inicio, fim+1, passo):
        print(f'{contador} ', end='', flush=True)
        sleep(0.5)
    print()


#Programa Principal
borda()
for contador in range(1, 11):
    print(f'{contador} ', end='', flush=True)
    sleep(0.5)
print('Fim!')
borda()
for contador in range(10, 0, -1):
    print(f'{contador} ', end='', flush=True)
    sleep(0.5)
print('Fim!')
borda()
print('Agora é sua vez de personalizar a contagem!')
inicio= int(input('Início: '))
fim= int(input('Fim: '))
passo= int(input('Passo: '))
borda()
Contagem(inicio, fim, passo)
borda()