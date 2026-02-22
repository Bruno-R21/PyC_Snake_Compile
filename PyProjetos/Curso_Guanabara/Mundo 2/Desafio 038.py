'''(Desafio 38) Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
> O PRIMEIRO VALOR é MAIOR.
> O SEGUNDO VALOR é MAIOR.
> NÃO EXISTE valor maior, os dois são iguais.'''

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

if num1 > num2:
    print(f'\nO primeiro número é o maior!\n')

elif num1 < num2:
    print(f'\nO segundo número é o maior!\n')

else:
    print(f'\nOs dois números são iguais, não há maior!\n')

