# (Desafio 27) Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Informe o seu nome completo: ')).strip()
nome = nome.split()

primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print(f'O seu primeiro nome é: {primeiro_nome}')
print(f'O seu último nome é: {ultimo_nome}')



