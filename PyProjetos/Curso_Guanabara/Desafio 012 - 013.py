#(Desafio 12) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. Com 5%, 10% e 20% de desconto.

#preco = float(input('Informe o preço do produto: R$'))
#preco_5 = (preco * 0.95)
#preco_10 = (preco * 0.90)
#preco_20 = (preco * 0.80)

#print(' O preço normal do produto é: R$ {:.2f}, com desconto de 5% ele passou a ser: R$ {:.2f}'.format(preco, preco_5))
#print(' \nO preço normal do produto é: R$ {:.2f}, com desconto de 10% ele passou a ser: R$ {:.2f}'.format(preco, preco_10))
#print(' \nO preço normal do produto é: R$ {:.2f}, com desconto de 20% ele passou a ser: R${:.2f}'.format(preco, preco_20))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#(Desafio 13) Faça um algoritmo que leia o salário do funcionário e mostre o seu novo salário, já com o reajuste de 5,10%. Acrescente também um adicional de 30%, um anuênio, um diferencial de mercado, o vale transporte e ao final, calcule o valor total bruto que o funcionário irá receber. 

salario = float(input('Informe o seu salário atual: R$'))
novoSalario = salario + (salario * 5.10/100)
adicional30 = (novoSalario * 0.30)
anuenio = (novoSalario * 0.16)
diferencial = 96.00
valeTransporte = 197.40

print(' O salário atual é de: R$ {:.2f}, \nCom o reajuste, o seu novo salário passou a ser: R$ {:.2f}'.format(salario, novoSalario))

print('\nSomando o novo salário: R$ {:.2f} + \nAdicional de 30%: R$ {:.2f} + \nAnuênio: R$ {:.2f} + \nDiferencial de mercado: R$ {:.2f} + \nVale tranporte: R$ {:.2f} \nO valor total é de: {:.2f}'.format(novoSalario, adicional30, anuenio, diferencial, valeTransporte, (novoSalario + adicional30 + anuenio + diferencial + valeTransporte))) 

