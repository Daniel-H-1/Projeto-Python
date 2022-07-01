print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Faç um programa que sorteie números aleatórios. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('SORTEANDO NÚMEROS')
print('-' * 40)
from random import randint
from time import sleep
Sorteio = []
temporária = []
quantidade = int(input('Quantos sorteios você quer fazer? R:'))
#Laço para fazer o sorteio de acordo com a quantidade
for intervalo in range(0, quantidade):
    #Laço para colocar os números na lista sorteio temporária
    for c in range(0, 6):
        aleatório = randint(1, 60)
        if c == 0:
            temporária.append(aleatório)
        elif temporária.count(aleatório) > 0:
            while temporária.count(aleatório) > 0:
                aleatório = randint(0, 60)
            temporária.append(aleatório)
        else:
            temporária.append(aleatório)
    Sorteio.append(temporária[:])
    temporária.clear()
for repetição in range(0, quantidade):
    print(Sorteio[repetição])
    sleep(1)

