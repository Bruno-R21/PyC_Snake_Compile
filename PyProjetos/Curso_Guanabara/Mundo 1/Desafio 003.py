#Como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). (Aula 6)

# n1 = input('Digite um valor:')
# print(type(n1))
# Digite um valor: 21
# <class 'str'> 

# n1 = int(input('Digite um valor:'))
# print(type(n1))
# Digite um valor:21
# <class 'int'>

# Crie um programa que leia dois números e mostre a divisão entre eles.

n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))

d = (n1/n2)

print('O resultado da divisão de {} por {} é {:.2f}'.format(n1, n2, d))



