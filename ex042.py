a = int(input('Digite o primeiro lado: '))
b = int(input('digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and a == c and b == c:
        print('As medidas informadas formam um triângulo Equilátero!')
    elif (a == b) or ( a == c) or (b == c):
        print('As medidas informadas formam um triângulo Isóceles!')
    else:
        print('As medidas informadas formam um triângulo Escaleno!')
else:
    print('As medidas informadas não formam um triângulo!')