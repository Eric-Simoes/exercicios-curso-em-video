print(50 *'=')
valor = float(input('Insira o valor da casa: '))
Salario = float(input('Insira o valor do salário: '))
parcela = int(input('Informe quantas parcelas serão: '))

QuantP = valor / parcela
LimiteV = Salario * 0.3

if QuantP > LimiteV:
    print('Infelizmete não será possível realizar seu empréstimo!')
else:
    print('Parabéns seu empréstimo foi aprovado!')