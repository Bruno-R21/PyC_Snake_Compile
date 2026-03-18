'''(Desafio 43) Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
=> Abaixo de 18.5: ABAIXO DO PESO.
=> Entre 18.5 e 25: PESO IDEAL.
=> Entre 25 e 30: SOBREPESO.
=> Entre 30 e 40: OBESIDADE.
=> Acima de 40: OBESIDADE MÓRBIDA.'''

nome = str(input('Digite o nome da pessoa: '))
peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'ABAIXO DO PESO.'
elif imc >= 18.5 and imc < 25: 
    status = 'PESO IDEAL.' 
elif imc >= 25 and imc < 30:
    status = 'SOBREPESO.' 
elif imc >= 30 and imc <= 40:  
    status = 'OBESIDADE.'  
else:
    status = 'OBESIDADE MÓRBIDA.'  

print('\n' + '=' * 25 + ' MONITOR DE SAÚDE v1.0 (IMC) ' + '=' * 25)
print(f'\nDados informados: Peso => {peso} Kg e Altura => {altura} Metros.\n')
print(f'Ola {nome}! é um prazer te ver por aqui. \nBaseado no seu peso e altura, calculamos que o seu IMC é de: {imc:.1f}. \nIsso significa que você está na categoria: {status}.\n')

