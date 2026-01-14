# (Desafio 19) Um professor quer sortear um dos seus oito alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

'''from random import choice
nome1 = str(input('Informe o nome do primeiro aluno: '))
nome2 = str(input('Informe o nome do segundo aluno: '))
nome3 = str(input('Informe o nome do terceiro aluno: '))
nome4 = str(input('Informe o nome do quarto aluno: '))

lista = [nome1, nome2, nome3, nome4] 
vencedor = choice(lista)
print('\nO aluno escolhido para apagar o quadro foi: {}'.format(vencedor))'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# (Desafio 20) Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle
nome1 = str(input('Informe o nome do primeiro aluno: '))
nome2 = str(input('Informe o nome do segundo aluno: '))
nome3 = str(input('Informe o nome do terceiro aluno: '))
nome4 = str(input('Informe o nome do quarto aluno: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('\nA ordem de apresentação dos trabalhos será: {}'.format(lista))




