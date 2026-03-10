'''(Desafio 42) Crie um programa que peça ao usuário o comprimento de três lados de um triângulo e verifique se esses valores podem formar um triângulo, mostrando qual tipo de triângulo será formado:
=> EQUILÁTERO: Todos os lados iguais.
=> ISÓSCELES: Dois lados iguais.
=> ESCALENO: Todos os lados diferentes.'''

lado_a = float(input('Digite o comprimento do primeiro lado: '))
lado_b = float(input('Digite o comprimento do segundo lado: '))
lado_c = float(input('Digite o comprimento do terceiro lado: '))

if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    if lado_a == lado_b == lado_c:
        mensagem = 'todos os lados iguais'
        tipo = 'Equilátero'
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        mensagem = 'dois lados iguais'
        tipo = 'Isósceles'
    elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c: 
        mensagem = 'todos os lados diferentes'  
        tipo = 'Escaleno'

    print(f'\nOs comprimentos informados podem formar um triângulo {tipo}. \nEsse é um triângulo que tem {mensagem}.\n')   

else:
    print('\nOs valores informados NÃO PODEM FORMAR um triângulo.') 



