print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora  o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from random import randint

número = randint(0, 10)
acertou = False
tentativas = 0
print('Computador já sorteiou um número!!!')

while not acertou:
    palpite = int(input('Qual foi o número que ele escolheu? '))
    tentativas += 1
    if palpite == número:
        acertou = True
    else:
        if palpite < número:
            print('O valor que o Computado sorteiou é MAIOR!')
        elif palpite > número:
            print('O valor que o computado sorteiou é MENOR')
print('Acertou com {} Tentativas'.format(tentativas))
print('>>>>> FIM <<<<<')
