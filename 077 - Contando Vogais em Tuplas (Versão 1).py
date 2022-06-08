print('=' * 40)
print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie uma tupla que tenha diversas palavras(Não use acentos),
e mostre as vogais de cada palavra.''')

print('=' * 40)
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('PALAVRAS E SUAS VOGAIS')
print('-' * 40)
Palavras = ('ABACAXI', 'MORANGO', 'MANGA', 'CAMINHO', 'FUTEBOL'
            'TAMANDUA', 'GORILA', 'CARROS', 'JOGOS', 'ACABOU')
for pos in range(0, len(Palavras)):
    print(f'As vogais da palavra {Palavras[pos]} são: ', end='')
    if Palavras[pos].count('A') >= 1:
        print('A ', end='')
    if Palavras[pos].count('E') >= 1:
        print('E ', end='')
    if Palavras[pos].count('I') >= 1:
        print('I ', end='')
    if Palavras[pos].count('O') >= 1:
        print('O ', end='')
    if Palavras[pos].count('U') >= 1:
        print('U ', end='')
    print(' ')
print('-' * 40)
print(f'{"FIM":=^40}')
