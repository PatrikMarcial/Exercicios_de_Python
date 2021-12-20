'''.Faça um programa que leia 5 números inteiros positivos e informe a soma e a
média dos números.'''

soma = 0
for a in range(1, 5+1):
    b = int(input('Me diga um numero inteiro: '))
    soma += b
print(f'a média desses numeros é de {soma/5}')

