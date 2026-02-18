'''(Desafio 36) Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. 
> A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor = float(input('Qual é o valor de venda da casa? R$'))
salário = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos ele irá pagar? '))

if anos <= 0:
    print('\nQuantidade de anos inválida.\n') 
else:
    meses = anos * 12
    prestação = valor / meses
    limite = (salário * 0.30)

    if prestação <= limite:      
        print(f'\nO seu empréstimo foi APROVADO! \nO valor da sua prestação mensal será de R${prestação:.2f}. \nO valor do empréstimo será quitado em {meses} meses.\n')
    else:
        print(f'\nO valor da prestação é de R${prestação:.2f}. \nQue pena! \nEsse valor excedeu o limite de 30% do seu salário que é de R${limite:.2f}. \nSendo assim, o empréstimo foi negado.\n')



