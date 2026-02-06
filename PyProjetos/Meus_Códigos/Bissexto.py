import random

vidas = 3
pontos = 0
nivel = 1

print('🧙‍♂️ Bem-vindo ao Guardião dos Anos!')
print('Descubra se o ano é bissexto para subir de nível.')
print('Digite S para SIM ou N para NÃO.')

while vidas > 0 and nivel <= 3:

    print(f'\n=== NÍVEL {nivel} ===')
    print(f'Vidas: {vidas} | Pontos: {pontos}')

    # Dificuldade por nível
    if nivel == 1:
        ano = random.randint(2000, 2030)
    elif nivel == 2:
        ano = random.randint(1900, 2100)
    else:
        ano = random.randint(1, 3000)

    print(f'O ano é: {ano}')
    resposta = input('É bissexto? (S/N): ').upper()

    # Resposta correta
    if ano % 4 == 0:
        correto = 'S'
    else:
        correto = 'N'

    # Verificação
    if resposta == correto:
        print('Acertou! +10 pontos ⭐')
        pontos += 10
    else:
        print('Errou! -1 vida 💔')
        vidas -= 1

    # Subir de nível a cada 30 pontos
    if pontos >= nivel * 30:
        nivel += 1
        print('✨ Você subiu de nível!')

# Final do jogo
print('\n=== FIM DE JOGO ===')

if vidas == 0:
    print('Suas vidas acabaram...')
else:
    print('Parabéns! Você completou todos os níveis!')

print(f'Pontuação final: {pontos}')
