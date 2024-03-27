num = int(input('Digite um número: '))
print('A tabuada do número escolhido é')
for c in range(1, 11):
    s = num * c
    print('{} x {} = {}'. format(num, c, s) )