'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro.'''

nome = input('Digite seu nome de usario: ')
senha = input('Digite uma senha: ')
if nome == senha:
    print('Erro, A sua senha não pode ser a mesma do nome de usuario!')
else:
    print(f'Seu nome de usuario é {nome} e sua senha é {senha}.')



