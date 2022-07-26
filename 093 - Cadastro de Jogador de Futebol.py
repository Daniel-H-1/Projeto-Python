print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário,  incluindo o total de gols feitos durante o campeonato.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('ESTATÍSTICAS DE JOGADOR')
print('-' * 40)
partidas = list()
jogador = dict()
totaldegols = 0

jogador['Nome'] = str(input('Nome: '))
jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for v in range(1, (jogos + 1)):
    partidas.append(int(input(f' Quantos gols foram feitos na partida {v}: ')))
jogador['Gols'] = partidas[:]
jogador['Total de Gols'] = sum(jogador["Gols"])
print(f'{"INFORMAÇÕES":-^40}')
print(jogador)
print(f'{"Keys e Valeus":-^40}')
for k, v in jogador.items():
    print(f'{k} tem o valor: {v}')
print(f'{"Gols nas Partidas":-^40}')
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for pos, valor in enumerate(jogador["Gols"]):
    print(f' >>> Na partida {pos + 1}, fez {valor} gol(s).')
print(f' No total {jogador["Nome"]} fez {jogador["Total de Gols"]} gols.')
print(f'{"FIM":=^40}')

