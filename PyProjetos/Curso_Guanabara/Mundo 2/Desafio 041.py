'''(Desafio 41) A confederação Brasileira de Natação precisa de um programa que leia o ano de NASCIMENTO de um atleta e mostre sua CAREGORIA, de acordo com a idade:
=> Até 9 anos: MIRIM.       => Até 14 anos: INFANTIL.
=> Até 19 anos: JUNIOR.     => Até 25 anos: SÊNIOR.
=> Acima de 25 anos: MASTER.'''

# Evolução do do código realizada no ChatGPT.
from datetime import datetime

ano_nascimento = int(input('Qual o ano de nascimento do atleta? '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

print('\n' + '=' * 27 + ' DADOS DA CATEGORIA ' + '=' * 27)

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'''
O atleta nasceu em {ano_nascimento}
A idade é {idade} anos
A categoria é: {categoria}
''')

# O código como eu fiz sem ajuda da IA.

'''from datetime import datetime

ano_nascimento = int(input('Qual o ano de nascimento do Atleta? '))
ano_atual = datetime.now().year 
idade = ano_atual - ano_nascimento
print('\n'+'=' * 27 + 'DADOS DA CATEGORIA' + '=' * 27)

if idade <= 9:
    print(f'\nO Atleta nasceu em {ano_nascimento}, \nA sua idade é de {idade} anos, \nA sua categoria é: MIRIM.\n')
elif idade <= 14:
     print(f'\nO Atleta nasceu em {ano_nascimento}, \nA sua idade é de {idade} anos, \nA sua categoria é: INFANTIL.\n')   
elif idade <= 19:
     print(f'\nO Atleta nasceu em {ano_nascimento}, \nA sua idade é de {idade} anos, \nA sua categoria é: JUNIOR.\n')    
elif idade <= 25:
     print(f'\nO Atleta nasceu em {ano_nascimento}, \nA sua idade é de {idade} anos, \nA sua categoria é: SÊNIOR.\n') 
else:
     print(f'\nO Atleta nasceu em {ano_nascimento}, \nA sua idade é de {idade} anos, \nA sua categoria é: MASTER.\n')'''     







