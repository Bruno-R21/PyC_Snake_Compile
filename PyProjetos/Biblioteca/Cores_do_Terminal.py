'''**********ALTERANDO AS CORES DO TERMINAL EM PYTHON**********

> STYLE                       
0 (NONE)
1 (BOLD)
4 (UNDERLINE)
7 (NEGATIVE)

> COR            > TEXT (CÓDIGO)              > BACK (CÓDIGO)
BRANCO                  30                            40
VERMELHO                31                            41
VERDE                   32                            42 
AMARELO                 33                            43
AZUL                    34                            44
LILÁS                   35                            45
AZUL CLARO              36                            46
CINZA                   37                            47

> EXEMPLO:
             \033[0;33;44m'''

# >>>>>>>>>>>>>>>       NA PRÁTICA      >>>>>>>>>>>>>>>>>>>>>>>

print('\033[0;33;47mOlá, Bruno!')
print('\033[1;31;43mComo você esta?')
print('\033[4;30;46mEstou bem, curtindo minhas férias.')
print('\033[7;30mVou passear em Arraial do Cabo-RJ.')

nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))

print(f'Ola \033[33m{nome}\033[m, faltam \033[36m{65 - idade}\033[m anos para você chegar aos 65 anos.')



