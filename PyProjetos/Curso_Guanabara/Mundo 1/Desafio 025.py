# (Desafio 25) Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Qual o seu nome completo? '))

print("Seu nome tem Silva?", 'Silva' in nome.title())


'''nome = str(input('Qual o seu nome completo? ')).strip()
nome = nome.title()

tem_souza = 'Souza' in nome

if tem_souza:
    print('Parabéns! \nO \"Souza\" faz parte do seu nome. ')
else:
    print('Que pena! \nO \"Souza\" não faz parte do seu nome.')'''


