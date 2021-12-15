'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
que cada litro de tinta pinta uma área de 2 metros quadrados.(curso em video)'''

Largura = int(input('Me Diga a sua Largura: '))
Altura = int(input('Me diga sua Altura: '))
Area = Largura * Altura
tinta = Area/2
print(f'\na Área dessa parede é de {Area} metros quaadrados. Ela gastara {tinta} Litros de tinta para pintar essa parede.\n')
