print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
 sabendo que o vencedor tirou o maior número no dado.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('JOGO DE DADOS')
print('-' * 40)
from random import randint
from time import sleep
from operator import itemgetter
#Dicionário para colocar os valores dos dados.
informacoes = {'jogador 1': randint(1, 6),
               'jogador 2': randint(1, 6),
               'jogador 3': randint(1, 6),
               'jogador 4': randint(1, 6)}
for keys, values in informacoes.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(1)
print(f'{"RANKING":=^25}')

#Dicionário para colocar o Ranking em ordem.
ranking = dict()
#Ordenando o ranking para ter os daddos em ordem.
ranking = sorted(informacoes.items(), key=itemgetter(1), reverse=True)
#Mostrando o ranking com FOR.
for pos, valor in enumerate(ranking):
    print(f'{pos + 1}º Lugar: {valor[0]} com {valor[1]}')
    sleep(1)
print(f'{"FIM":=^40}')
