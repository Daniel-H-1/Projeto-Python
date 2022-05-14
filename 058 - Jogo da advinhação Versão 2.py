print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora  o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from random import randint

número = randint(0, 10)
palpite = 11

print('TENTE ADIVINHAR O NÚMERO ')
while palpite != número:
    print('=-' * 10)
    número = randint(0, 10)
    print('Computador já sorteiou um número!!!')
    palpite = int(input('Qual foi o número que ele escolheu? '))
    if palpite == número:
        print('Parabéns você acertou o palpite!!!')
    else:
        print('Tente Outra Vez.')
print('>>>>> FIM <<<<<')
print('{:>^15}'.format(' FIM '))

