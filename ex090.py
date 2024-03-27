boletim = {}
boletim['nome'] = str(input('Digite o nome do aluno: '))
boletim['nota'] = float(input('Digite a nota do aluno: '))
print(f'- nome {boletim["nome"]}')
print(f'- nota {boletim["nota"]}', end='')
print()
if boletim['nota'] < 4:
    print(f'- situação REPROVADO')
elif 4 > boletim['nota'] < 6:
    print('- situação RECUPERAÇÃO')
elif boletim['nota'] > 7:
    print('- sitação APROVADO')