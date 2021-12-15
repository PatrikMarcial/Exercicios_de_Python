'''
Faça um Programa que peça dois números e imprima o maior deles. Caso
sejam iguais, nada deverá ser exibido.
'''
numero = float(input('Me diga um numero: '))
numero2 = float(input('Me diga outro numero: '))
if numero > numero2:
    print(f'O numero {numero} é Maior que o numero {numero2}')
elif numero == numero2:
    print()
else:
    print(f'O numero {numero2} é Maior que o numero {numero}')
