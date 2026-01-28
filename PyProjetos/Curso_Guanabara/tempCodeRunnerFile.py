import unicodedata

frase = str(input('Escreva uma frase qualquer: '))
frase = frase.upper()

frase_nova = frase.replace(" ","")
frase_normal = unicodedata.normalize("NFD", frase_nova)

qtd_A  = frase_normal.count("A")
primeira = frase_normal.find("A")
ultima = frase_normal.rfind("A")

print(f'\nA letra \"A\" aparece {qtd_A} vezes na frase.')
print(f'\nA letra \"A\" aparece na posição {primeira}, pela primeira vez no texto.')
print(f'\nA letra \"A\" aparece na posição {ultima}, pela ultima vez no texto.')
