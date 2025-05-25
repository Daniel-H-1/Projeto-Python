print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Aprimore o  DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização
de DETALHES DO APROVEITAMENTO de cada jogador''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')

print("-" * 40)
print(f'{"ESTATÍSTICAS DO TIME": ^40}')
print('-' * 40)

# Definindo Listas, Dicionários e Variáveis
time = list()
partidas = list()
jogador = dict()


#Montando Loop para cadastro dos Jogadores
while True:

    # Nome, Partidas e Gols
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    # Adicionando as partidas e gols do Jogador
    partidas.clear()
    for v in range(1, (jogos + 1)):
        partidas.append(int(input(f' Quantos gols foram feitos na partida {v}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas)
    time.append(jogador.copy())

   # Quer continuar Adicionando mais jogadores?
    while True:
        print('')
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            print('-' * 30)
            break
        print('ERRO! Responda apenas S (SIM) ou  N (NÃO).')
    if resposta == 'N':
        break

print('-=' * 30) # Dividindo as Informações

# Apresentando os Nomes das Colunas, conforme as Keys do Dicionário Jogador
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('')

print('-' * 40) # Dividindo as Informações

# Apresentando o Nome, Gols por Partida e Total de Gols na TABELA
for key, valor in enumerate(time):
    print(f'{key:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()

print('-' * 40) # Dividindo as Informações


# Buscando o Jogador pelo Código para mostrar as estatísticas
while True:
    busca_de_jogador = int(input('Digite o Código do Jogador para ver suas Estatísticas (999 para Parar) '))
    if busca_de_jogador >= len(time):
        print(f'ERRO! Não existe jogador com código {busca_de_jogador}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca_de_jogador]["Nome"]}: ')
        for indice, gols in enumerate(time[busca_de_jogador]["Gols"]):
            print(f'   Na partida {indice+1} fez {gols} gols. ')
    print("-" * 40)


print(f'{"FIM":=^40}')