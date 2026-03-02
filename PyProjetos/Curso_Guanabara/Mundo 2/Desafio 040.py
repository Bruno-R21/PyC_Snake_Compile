'''(Desafio 40) Crie um programa que leia quatro notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-> Média abaixo de 5.0: REPROVADO.
-> Média entre 5.0 e 6.9: RECUPERAÇÃO.
-> Média 7.0 ou superior: APROVADO. '''

n1 = float(input('Digite a nota do 1° Bimestre: '))
n2 = float(input('Digite a nota do 2° Bimestre: '))
n3 = float(input('Digite a nota do 3° Bimestre: '))
n4 = float(input('Digite a nota do 4° Bimestre: '))

media = (n1+n2+n3+n4)/4
print()
print('=' * 27 + 'RESULTADO FINAL' + '=' * 27)
print(f'\nA sua média foi: {media}')

if media < 5.0:
    print('\nInfelizmente a sua média ficou abaixo de 5.0, você está REPROVADO.\n')
    print('\U0001F4E2 Não desista! Continue estudando.\n')

elif (media >= 5.0) and (media <= 6.9):
    print('\nA sua média ficou entre 5.0 e 6.9, você está de RECUPERAÇÃO.\n')
    print('\U0001F680 Revise a matéria e se prepare para a prova de recuperação!\n')

elif media >= 7.0:
    print('\nVocê alcançou uma média >= a 7.0, situação: APROVADO.\n')
    print('\U0001F389 Parabéns! Excelente desempenho, continue assim.\n')







