from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Vamos jogar JOKENPÔ!!!!')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua escolha:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 10)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=' * 10)

if computador == 0: #Se o computador escolher PEDRA.
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE!')
    elif jogador == 2:
        print('Computador VENCE!!')
    else:
        print('Escolha Inválida')
elif computador == 1: #Se o computador escolher PAPEL.
    if jogador == 0:
        print('Computador VENCE!!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE!!!')
    else:
        print('Escolha Inválida')
elif computador == 2: #Se o computador escolher TESOURA.
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE!!!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Escolha Inválida')