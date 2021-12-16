'''Faça um programa que calcule as raízes de uma equação do segundo grau, na
forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:
◦ Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e
o programa não deve fazer pedir os demais valores, sendo encerrado;
◦ Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao
usuário e encerre o programa;
◦ Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informa ao usuário;
◦ Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;'''

a = float(input('Me diga o valor de a: '))
if a == 0:
    print('O valor de a não pode ser igual a 0')
    exit()
b = float(input('Me diga o valor de b: '))
c = float(input('Me diga o valor de c: '))
delta = b**2 + (-4*a*c)
bask = delta ** 0.5
x1 = (-b +bask)/2*a
x2 = (-b -bask)/2*a
if delta < 0:
    print('O Delta é negativo, a equação não possui raizes reais.')
    exit()
elif delta == 0:
    if x1 > 0:
        print(f'O delta é {delta}, sua equação possui apenas uma raiz real que é {x1}')
    else:
        print(f'O delta é {delta}, sua equação possui apenas uma raiz real que é {x2}')
else:
    print(f'O Delta é {delta}, sua equação possui duas raizes reais, são {x1} e {x2}')











