'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados
formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
◦ Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
◦ Triângulo Equilátero: três lados iguais;
◦ Triângulo Isósceles: quaisquer dois lados iguais;
◦ Triângulo Escaleno: três lados diferentes;'''

lado1 = float(input('Me diga o valor do primeiro lado do Triângulo: '))
lado2 = float(input('Me diga o valor do segundo lado: '))
lado3 = float(input('Me diga o valor do terceiro lado: '))
equilatero = lado1 == lado2 == lado3

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print(f'É um triângulo Equilátero, pois todos os lados possuem o mesmo valor.')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print(f'É um triângulo Isósceles, pois dois lados possuem o mesmo valor e o outro lado é diferente.')
    else:
        print(f'É um triângulo Escaleno, pois todos os lados são diferentes.')
else:
    print('Os valores dos lados que você digitou, não pode formar um triângulo.!')



