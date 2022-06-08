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
Palavras = ('ABACAXI', 'MORANGO', 'MANGA', 'CAMINHO', 'FUTEBOL',
            'TAMANDUA', 'GORILA', 'CARROS', 'JOGOS', 'ACABOU')
for p in Palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in "AEIOU":
            print(letra, end=' ')
print(' ')
print('-' * 40)
print(f'{"FIM":=^40}')