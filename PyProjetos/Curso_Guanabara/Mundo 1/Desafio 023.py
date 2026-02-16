'''(Desafio 23) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex.: Digite um número: 2501
unidade: 1 - dezena: 0 - centena: 5 - milhar: 2'''

'''num = str(input('Digite um número qualquer, pode ser de 0 até 9999: '))
num.split()

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')

Obs: Desta maneira, quando colocamos menos de 4 dígitos, da erro e não sai o resultado esperado.'''

# Solicita ao usuário um número inteiro de 0 a 9999
num = int(input("Digite um número de 0 a 9999: "))

# A unidade é o último dígito do número
# O operador % 10 retorna o resto da divisão por 10
unidade = num % 10

# Remove o último dígito e pega o próximo
# // 10 remove a unidade
# % 10 pega a dezena
dezena = (num // 10) % 10

# Remove os dois últimos dígitos e pega a centena
centena = (num // 100) % 10

# Remove os três últimos dígitos e pega o milhar
milhar = (num // 1000) % 10

# Exibe o resultado na tela
print(f"unidade: {unidade} \ndezena: {dezena} \ncentena: {centena} \nmilhar: {milhar}")
