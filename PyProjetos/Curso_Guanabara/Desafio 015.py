# (Desafio 15) escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia + R$0,15 por KM rodado.

qtd_dias = int(input('Quantos dias o carro ficou alugado?'))
Km = float(input('Quantos KM ele rodou?'))

total_dia = 60.00 * qtd_dias
total_km = 0.15 * Km

print('O caro ficou alugado por {} dias. \nEle rodou {:.2f} Kms. \nO valor total a pagar pelo aluguel do carro será de: R$ {:.2f}'.format(qtd_dias, Km, (total_dia + total_km)))


