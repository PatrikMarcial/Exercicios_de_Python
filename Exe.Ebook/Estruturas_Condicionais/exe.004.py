'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme
a letra escrever: F - Feminino, M – Masculino'''

sexo = str(input('Digite Sua sexualidade (F) para Feminino e (M) para Masculino: ').upper())
if sexo == 'F':
    print('Seu sexo é Feminino')
elif sexo == 'M':
    print('Seu sexo é Masculino')
else:
    print()
