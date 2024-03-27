Dados_Trabalhistas = {}
Dados_Trabalhistas['nome'] = str(input('nome: '))
Dados_Trabalhistas['ano_nascimento']= int(input('Ano de nascimento: '))
Dados_Trabalhistas['carteira_de_trabalho']= int(input('Carteira de Trabalho (0 se não tem): '))
if Dados_Trabalhistas['carteira_de_trabalho'] == 0:
    print('-='*30)
    print(f'- nome tem o valor: {Dados_Trabalhistas["nome"]}')
    print(f'- ano de nascimento tem o valor: {Dados_Trabalhistas["ano_nascimento"]}')
    print(f'- não tem ctps')
else:
    Dados_Trabalhistas['ano_contratação']= int(input("Ano da Contratação: "))
    Dados_Trabalhistas['salário']= float(input("Salário: R$"))
    print(f'- nome tem o valor: {Dados_Trabalhistas["nome"]}')
    print(f'- ano de nascimento tem o valor: {Dados_Trabalhistas["ano_nascimento"]}')
    print(f'- ctps tem o valor: {Dados_Trabalhistas["carteira_de_trabalho"]}')
    print(f'- a contratação tem o valor: {Dados_Trabalhistas["ano_contratação"]}')
    print(f'- o salário tem o valor: {Dados_Trabalhistas["salário"]}')
