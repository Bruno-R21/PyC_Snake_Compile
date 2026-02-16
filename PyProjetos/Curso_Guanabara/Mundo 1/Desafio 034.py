'''(Desafio 34) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
> Para salários superiores a R$5.000,00, calcule um aumento de 10%.
> Para os inferiores ou iguais, o aumento será de 15%.'''

salario = float(input('Digite o salário do funcionário: R$'))

# Aqui você verifica o valor do salário e adiciona o percentual de aumento correspondente.
if salario > 5000:
    novo_salario = (salario * 1.10) 
else:
    novo_salario = (salario * 1.15) 

print(f'O salário antigo era de R${salario:.2f}. \nJá com o aumento aplicado, o novo salário passou a ser de: R${novo_salario:.2f}')    