'''(Desafio 30) Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro qualque: '))

resto = num % 2

if resto == 0:
    print(f'Você digitou o número {num} e ele é PAR.')
else:
    print(f'Você digitou o número {num} e ele é IMPAR.')'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#(Desafio 31) Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância percorrida na viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
    print(f'Você percorreu uma distância de {distancia}Km e \no valor da passagem ficou em R${preco:.2f}. ')
else:
    preco = distancia * 0.45
    print(f'Você percorreu uma distância de {distancia}Km e \no valor da passagem ficou em R${preco:.2f}. ')


