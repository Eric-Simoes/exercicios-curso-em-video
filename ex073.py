times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Os 5 primeiros colocados são{times[0:5]}')
print('-'*88)
print(f'Os últimos 4 colocados são {times[16:]}')
print('-'*88)
print(f'Os times são representado de forma alfabética dessa maneira{sorted(times)}')
print('-'*88)
print(f'O Chapecoense está na posição {times.index("Chapecoense")+1}')