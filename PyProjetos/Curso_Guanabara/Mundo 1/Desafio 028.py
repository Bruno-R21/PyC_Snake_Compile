# (Desafio 28) Escreva um programa que faça o computador "pensar" em um número inteiro ente 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint
num_cpu = randint(0, 5) # Faz o computador escolher um número aleatório.
from time import sleep 

print('-' * 75)
print('Adivinhe em qual número estou pensando!')
print('-' * 75)

num = int(input('Informe um número inteiro, entre 0 e 5: ')) # O Jogador escolhe um número e tenta acertar.
print('Processando...')
sleep(2) # O computador faz um mistério e só apresenta o resultado após 2 segundos.

if num == num_cpu:
    print(f'Parabéns, você venceu! \nO número que pensei foi o {num_cpu}, você digitou {num} e acertou.')

else: 
    print(f'Que pena, você perdeu! \nO número que pensei foi o {num_cpu}, você digitou {num} e errou. \nTente outra vez.')

