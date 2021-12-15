'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 8.9 B
Entre 6.0 e 7.4 C
Entre 4.0 e 5.9 D
Entre 3.9 e zero E
O algoritmo deve mostrar as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E.'''

nota1 = float(input('Me diga a primeira nota: '))
nota2 = float(input('Me diga a segunda nota: '))
media = (nota1 + nota2) / 2
if 9.0 <= media <= 10.0:
    print(f'Sua média no semestre foi de {media}, você ficou com A e foi APROVADO!')
elif 7.5 <= media <= 8.9:
    print(f'Sua média no semestre foi de {media}, você ficou com B e foi APROVADO!')
elif 6.0 <= media <= 7.4:
    print(f'Sua média no semestre foi de {media}, você ficou com C e foi APROVADO!')
elif 4.0 <= media <= 5.6:
    print(f'Sua média no semestre foi de {media}, você ficou com D e foi REPROVADO!')
else:
    print(f'Sua média no semestre foi de {media}, você ficou com E e foi REPROVADO!')






