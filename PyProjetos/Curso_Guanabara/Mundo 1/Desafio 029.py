'''(Desafio 29) Escreva um programa que leia a velocidade de um veículo. Se ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado. 
Se o excesso de velocidade for de até 20%, a infração será "MÉDIA", o valor será de R$130,16 e perde 4 pontos na CNH.
Se o excesso de velocidade for entre 20% e 50%, a infração será "GRAVE", o valor será de R$195,23 e perde 5 pontos na CNH.
Mas, se o excesso de velocidade for acima de 50%, a infração será "GRAVÍSSIMA", o valor será de R$880,41 e tem a suspensão imediata do direito de dirigir.'''

velocidade = int(input('digite a velocidade do veículo: '))
simbol = ('*' *75)

if velocidade <= 80:
    print(f'{simbol} \nParabéns! \nVeículo passou dentro da velocidade permitida.')
elif velocidade <= (80 *1.2):
    print(f'{simbol} \nExcesso de velocidade em até 20%! \nVocê foi multado em R$130,16 e perdeu 4 pontos na CNH.')  
elif velocidade <= (80 *1.5):
    print(f'{simbol} \nExcesso de velocidade entre 20% e 50%! \nVocê foi multado em R$195,23 e perdeu 5 pontos na CNH.')      
else:
    print(f'{simbol} \nExcesso de velocidade superior a 50%! \nVocê foi multado em R$880,41 \nSua CNH foi suspensa e perdeu o direito de dirigir.')    
