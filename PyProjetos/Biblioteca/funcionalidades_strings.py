'''Manipulando cadeia de textos (strings) em python
Fatiamento, Análise, Transformação, Divisão e Junção.'''
frase = "bruno em curso"

print('1º ->',frase[9:14]) #fatiamento da string para pegar a palavra "curso" --> obs: O "14" não é incluído, pega até o índice 13
print('1.1º ->',frase[:5]) #fatiamento da string para pegar a palavra "bruno" --> obs: O "5" não é incluído, pega até o índice 4
print('1.2º ->',frase[1:12:2]) #fatiamento da string com passo 2
print('2º ->',frase.count("u")) #conta quantas vezes o caractere "u" aparece na string
print('3º ->',frase.replace("bruno", "Bruno")) #substitui a palavra "bruno" por "Bruno" na string --> obs: A string original não é alterada, para alterar a string original é necessário atribuir o resultado a uma nova variável ou à própria variável original - frase = frase.replace("bruno", "Bruno")
print('4º ->',frase.upper()) #converte todos os caracteres da string para maiúsculo
print('5º ->',frase.lower()) #converte todos os caracteres da string para minúsculo
print('6º ->',frase.capitalize()) #converte o primeiro caractere da string para maiúsculo
print('7º ->',frase.title()) #converte o primeiro caractere de cada palavra para maiúsculo
print('8º ->',frase.strip()) #remove espaços em branco no início e no fim da string
print('9º ->',frase.split()) #divide a string em uma lista de palavras
print('10º ->','-'.join(frase)) #junta os caracteres da string com o caractere "-" entre eles
print('11º ->',frase.find("curso")) #retorna a posição inicial da palavra "curso" na string
print('12º ->',frase.index("curso")) #retorna a posição inicial da palavra "curso" na string
print('13º ->',frase.startswith("bruno")) #verifica se a string começa com a palavra "bruno"
print('14º ->',frase.endswith("curso")) #verifica se a string termina com a palavra "curso"
print('15º ->',frase.isnumeric()) #verifica se todos os caracteres da string são numéricos
print('16º ->',frase.isalpha()) #verifica se todos os caracteres da string são alfabéticos
print('17º ->',frase.isalnum()) #verifica se todos os caracteres da string são alfanuméricos
print('18º ->',frase.islower()) #verifica se todos os caracteres da string estão em minúsculo
print('19º ->',frase.isupper()) #verifica se todos os caracteres da string estão em maiúsculo
print('20º ->',len(frase)) #retorna o tamanho da string 
print('21º ->',frase.count("o")) #conta quantas vezes o caractere "o" aparece na string
print('22º ->',frase[0:5])  #fatiamento da string para pegar a palavra "bruno"  
print('23º ->',frase.split()[2])    #divide a string em uma lista de palavras e pega a terceira palavra "curso"    
print('24º ->',frase.split()[0])    #divide a string em uma lista de palavras e pega a primeira palavra "bruno"
print('25º ->',frase.replace("curso", "aula").upper())  #substitui a palavra "curso" por "aula" e converte todos os caracteres para maiúsculo
print('26º ->',frase.capitalize().replace("bruno", "Bruno"))    #converte o primeiro caractere para maiúsculo e substitui "bruno" por "Bruno"
print('27º ->',frase.title().replace("Curso", "Aula"))  #converte o primeiro caractere de cada palavra para maiúsculo e substitui "Curso" por "Aula"
print('28º ->',frase.strip().capitalize())  #remove espaços em branco no início e no fim da string e converte o primeiro caractere para maiúsculo
print('29º ->',frase.find("em"))    #retorna a posição inicial da palavra "em" na string
print('30º ->',frase.index("curso"))    #retorna a posição inicial da palavra "curso" na string
