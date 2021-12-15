'''Faça um programa para a leitura de duas notas parciais de um aluno. O
programa deve calcular a média alcançada por aluno e apresentar:
 ◦ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 ◦ A mensagem "Reprovado", se a média for menor do que sete;'''

nota1 = float(input('Me diga a primeira nota: '))
nota2 = float(input('Me diga a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Você teve a Média igual a {media}')
    print('Parabens, você foi Aprovado!!!')
else:
    print(f'Você teve a Média igual a {media}')
    print('Eu lamento dizer, você foi Reprovado!')
