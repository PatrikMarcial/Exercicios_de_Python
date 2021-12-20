'''Criar um programa que leia dez números inteiros e imprima o maior e o menor
número da lista'''

quant = maior = menor = 0
for a in range(1, 11):
    num = int(input('Me diga um numero: '))
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O maior e menor valor desses numeros digitados foram {maior} e {menor}')