# (Desafio 24) Crie um programa que leia o nome de uma cidade e diga se ela começa com "Santo".

'''cidade = str(input('Digite o nome da cidade que você nasceu? '))
cidade = cidade.strip()
cidade = cidade.capitalize()

resultado = cidade.startswith('Santo')

if resultado: 
    print(f'Sim, a cidade escolhida foi {cidade} e \no seu nome começa com a palavra \"Santo\".')
else: 
    print(f'Não, a cidade escolhida foi {cidade} e \no seu nome não começa com a palavra \"Santo\". ')'''

cidade = str(input('Em qual cidade você nasceu? ')).strip()
cidade = cidade.capitalize()

if (cidade[:5] =='Santo') or (cidade[:3] =='São'):
    print('true')
else:
    print('false')







    

