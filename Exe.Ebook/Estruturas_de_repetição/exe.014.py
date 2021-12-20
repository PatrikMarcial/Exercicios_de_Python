'''Criar um programa que leia um número (NUM), e depois leia NUM números
inteiros e imprima o maior deles. Suponha que todos os números lidos serão
positivos.'''

quant = maior = 0
a = int(input('Me diga a quantidade de numeros inteiros que você quer ler: '))
for b in range(1, a+1):
    num = int(input('Me diga um numero: '))
    quant += 1
    if quant == 1:
        maior = num
    else:
        if num > maior:
            maior = num
print(f'O maior valor desses números é {maior}')





