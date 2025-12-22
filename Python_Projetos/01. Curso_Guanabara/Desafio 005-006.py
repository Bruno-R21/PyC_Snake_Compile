# (Desafio 05) Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

# num = int(input('Digite um número:'))

#print('O número digitado foi: {} \n O seu antecessor é: {} \n O seu sucessor é: {}'.format(num, num-1, num+1))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# (Desafio 06) Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))

print('O número digitado foi: {}, \nO seu dobro é: {}, \nO seu triplo é:{} e \nA sua raiz quadrada é:{:.2f}'.format(n, (n*2), (n*3), pow(n, (1/2))))

# (n**(1/2))