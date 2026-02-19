'''(Desafio 37) Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
    > 1 para BINÁRIO
    > 2 para OCTAL
    > 3 para HEXADECIMAL'''

num = int(input('\nDigite um número inteiro: '))

print(25 * '-' + 'BASE DE CONVERSÃO' + 25 * '-')

print('''Digite 1 para "Binário". 
Digite 2 para "Octal". 
Digite 3 para "Hexadecimal".''')

codigo = int(input('\nDigite o codigo: '))

while codigo <= 0 or codigo > 3:
    print('Opção inválida! \nDigite um codigo válido:')
    codigo = int(input('\nDigite o codigo: '))

if codigo == 1:
    print(f'\nO número {num}, convertido em Binário é: {num:b}')

elif codigo == 2:
    print(f'\nO número {num}, convertido em Octal é: {num:o}')
    
else:
    print(f'\nO número {num}, convertido em Hexadecimal é: {num:x}')

print('\n')




