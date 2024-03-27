r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('As medidas digitas formam triângulo!')
else:
    print('As medidas digitadas não formam um triângulo!')
