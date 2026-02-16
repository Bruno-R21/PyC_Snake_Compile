#(Desafio 33) Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.  

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

# Descobrindo o maior.
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
    
# Descobrindo o menor.
menor = n1    
if n2 < menor:
    menor = n2  
if n3 < menor:
    menor = n3

print(f'O maior número é o: {maior}')
print(f'O menor número é o: {menor}')

