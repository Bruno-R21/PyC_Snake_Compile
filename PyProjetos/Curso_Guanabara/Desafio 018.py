# (Desafio 18) Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite o valor do ângulo: '))

print('O ângulo informado foi: {} \nO valor do seno é: {:.2f}\nO valor do cosseno é: {:.2f} \nA tangente desse ângulo é: {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))

