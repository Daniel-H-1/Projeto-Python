print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie uma tupla preenchida com os 20 times da série A do Campeonato Brasileiro
de acordo com a ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros.
B) Os último 4 colocados.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time do Bragantino.''')

print('=' * 40)
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
TIMES = ('Corinthias', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avaí',
         'América-MG', 'Palmeiras', 'Bragantino', 'Internacional', 'Fluminense', 'Goiás',
         'Cuiabá', 'Athletico-PR', 'Flamengo', 'Juventude', 'Ceará SC', 'Atlético-GO', 'Fortaleza')
print('OS 5 PRIMEIROS SÃO:')
print(TIMES[:5])
print('OS ÚLTIMOS 4 COLOCADOS SÃO:')
print(TIMES[-4:])
print('OS TIMES EM ORDEM ALFABÉTICA:')
print(sorted(TIMES))
print('O TIME DO BRAGANTINO ESTÁ NA COLOCAÇÃO:')
print(TIMES.index('Bragantino') + 1)
