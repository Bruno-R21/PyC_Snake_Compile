'''(Desafio 39) Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele AINDA VAI SE ALISTAR ao serviço militar, se é a HORA DE SE ALISTAR ou seja PASSOU DO TEMPO do alistamento.
O seu programa também deverá mostra o tempo que falta ou que passou do prazo.'''
from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year 
    idade = ano_atual - ano_nascimento
    return idade

nome = input('Qual o seu primeiro nome? ')
ano = int(input('Qual o seu ano de nascimento? '))
idade = calcular_idade(ano)

print(f'\nOlá {nome}, Você tem {idade} anos.')

if idade < 18:
    falta = 18 - idade
    print(f'Ainda não está no tempo de se alistar. \n Faltam {falta} anos.\n')
elif idade == 18:
    print(f'Está na hora, vai logo se alistar!\n')
else:
    passou = idade - 18
    print(f'Já passaram {passou} anos do prazo de alistamento.\n')


