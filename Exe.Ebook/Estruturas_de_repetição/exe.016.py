'''Escreva um programa, que leia um conjunto de 10 fichas, cada uma contendo,
a altura e o código do sexo de uma pessoa (código = 1 se for masculino e 2 se
for feminino), e calcule e imprima:
○ a maior e a menor altura da turma;
○ a média de altura das mulheres;
○ a média de altura da turma.'''

quant = quant2 = maior = menor = soma2 = soma= 0
for a in range(1, 11):
    altura = float(input('Me diga sua altura: '))
    sexo = int(input('Digite 1 para masculino e 2 para feminino(1/2): '))
    soma += altura
    quant += 1
    if sexo == 2:
        soma += sexo
        quant2 += 1
    if sexo == 1:
        print('masculino')
    else:
        print('femenino')
    if quant == 1:
        maior = menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura

print(f'A maior altura dessas fichas é {maior} e a menor altura é {menor}')
print(f'A media de altura da turma é {soma/10}')
if sexo == 2:
    print(f'A media de altura das mulheres é {soma/ quant2}')
else:
    print('Em nehuma das fichas citadas teve mulheres inscritas.')










