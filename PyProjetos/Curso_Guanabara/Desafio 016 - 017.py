# (Desafio 16) Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua parte inteira.

'''import math
num = float(input('Digite um número real: '))
n1 = math.trunc(num)
print(' O número digitado foi {} e a sua parte inteira é: {}'.format(num, n1)))'''

'''num = float(input('Digite um número real: '))
print('O número digitado foi {} e a sua parte inteira é: {}'.format(num, int(num)))'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# (Desafio 17) Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cop = float(input('Informe o cateto opsto: '))
cad = float(input('Informe o cateto adjacente: '))

hip = hypot(cop, cad)

print('O cateto oposto é: {} \nO cateto adjacente é: {} \nO comprimento da hipotenusa foi de: {:.2f}'.format(cop, cad, hip))


