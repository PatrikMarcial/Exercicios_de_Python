'''Uma empresa resolveu dar um aumento de salário aos seus colaboradores e
deseja te contratar para desenvolver o programa que calculará os reajustes. O
programa deve receber, via teclado, o salário de um colaborador. O percentual
de reajuste é dado segundo os critérios abaixo:
 ◦ salários até R$ 1500,00 (incluindo) : aumento de 20%
 ◦ salários entre R$ 1500,01 e R$ 2700,00 : aumento de 15%
 ◦ salários entre R$ 2700,01 e R$ 3500,00 : aumento de 10%
 ◦ salários de R$ 3500,01 em diante : aumento de 8%
Após o cálculo do reajuste, informe na tela:
 ◦ o salário antes do reajuste;
 ◦ o percentual de reajuste aplicado;
 ◦ o valor do aumento;
 ◦ o novo salário, após o reajuste'''

salario = float(input('Me diga o seu salário atual: '))
s1500 = (salario * 20/100) + salario
s2700 = (salario * 15/100) + salario
s3500 = (salario * 10/100) + salario
s35001 = (salario * 8/100) + salario
if salario <= 1500.00:
    print(f'O seu antigo salário era de {salario}R$, agora com o reajuste seu salário atual é de {s1500}R$')
elif 1500.01 <= salario <= 2700.00:
    print(f'O seu antigo salário era de {salario}R$, agora com o reajuste seu salário atual é de {s2700}R$')
elif 2700.01 <= salario <= 3500.00:
    print(f'O seu antigo salário era de {salario}R$, agora com o reajuste seu salário atual é de {s3500}R$')
else:
    print(f'O seu antigo salário era de {salario}R$, agora com o reajuste seu salário atual é de {s35001}R$')








