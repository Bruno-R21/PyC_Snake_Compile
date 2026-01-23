'''(Desafio 22) Crie um programa que leia o nome completo de uma pessoa e mostre: 
> O nome com todas as letras maiúculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()
nome_sem_espaco = len(nome) - nome.count(" ")

print(f'Em letras maiúsculas: {nome.upper()}')
print(f'Em letras minúsculas: {nome.lower()}')
print('Quantas letras tem o nome completo:' , nome_sem_espaco)
print('O seu 1º nome tem: {} letras'.format(nome.find(' ')))
print('Quantas letras tem o 2º nome:', len(nome.split()[1]))




      






