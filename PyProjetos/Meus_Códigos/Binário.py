'''Crie um programa para praticar o uso do print() junto com f-strings. Imprima, formatando, os seguintes dados:

> 10 (em decimal)
> 10 (de decimal, convertido em binário)
3.14159265 (com todas as casas decimais)
3.14159265 (com 2 casas decimais)'''

numero = 10
valor = 3.14159265 

print(f'O número é: {numero}')
print(f'O número {numero}, convertido em binário é: {numero:b}')
print(f'Mostrando na tela o valor {valor}')
print(f'Mostrando só com 2 casas decimais {valor:.2f}')

