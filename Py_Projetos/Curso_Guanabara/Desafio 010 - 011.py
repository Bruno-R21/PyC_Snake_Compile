 # (Desafio 10) Crie um programna que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar com esse valor.

# real = float(input('Quantos reais você tem na carteira? R$'))
# dolar = (real / 5.48)
#euro = (real / 6.44)

#print('Você tem R$ {:.2f} \nPode comprar US$ {:.2f} \nPode comprar £$ {:.2f}'.format(real, dolar, euro))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# (Desafio 11) Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para ointá-la. Sabemos que cada litro de tinta, pinta uma área de 2m².

largura = (float(input('Digite a largura da parede em metros:')))
altura = (float(input('Digite a altura da parede em metros:')))

area = (largura * altura) 
qtd_tinta = (area / 2)


print('Medidas da parede: \nLargura: {:.2f} metros. \nAltura: {:.2f} metros. \nÁrea: {:.2f} metros². \nA quantidade necessária de tinta para pintá-la, será de: {:.2f} litros.'.format(largura, altura, area, qtd_tinta))