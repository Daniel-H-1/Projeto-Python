print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final Mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas. ( Maior ou igual a 85Kg)
C) Uma listagem com as pessoas mais leves. (Menor ou igual a 70Kg)''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('ESTATÍSTICAS COM LISTAS')
Pessoas = list()
Dados_Pessoas = list()
Leves = list()
Pesadas = list()
total = menor = maior = 0
while True:
    print('-' * 40)
    Dados_Pessoas.append(str(input('Digite seu Nome: ')))
    Dados_Pessoas.append(int(input('Digite seu Peso: ')))
    if total == 0:
        maior = menor = Dados_Pessoas[1]
    else:
        if Dados_Pessoas[1] < menor:
            menor = Dados_Pessoas[1]
        if Dados_Pessoas[1] > maior:
            maior = Dados_Pessoas[1]
    Pessoas.append(Dados_Pessoas[:])
    Dados_Pessoas.clear()
    total += 1
    resposta = str(input('Quer cadastrar outra pessoa [S/N]: ')).strip()[0]
    while resposta not in 'SsNn':
        print('Resposta Inválida!')
        resposta = str(input('Quer cadastrar outra pessoa [S/N]: ')).strip()[0]
    if resposta in 'Nn':
        break
for valor in Pessoas:
    if valor[1] <= 70:
        Leves.append(valor[0])
    elif valor[1] >= 85:
        Pesadas.append(valor[0])
print('-' * 40)
print(f'Foram cadastradas {total} pessoas.')
#print(f'Você cadastrou {len(Pessoas}.')
print(f'As pessoas mais leves cadastradas são: {Leves}')
print(f'As pessoas mais pesadas cadastradas são: {Pesadas}')
print(f'O(s) menor(es) peso(s) é {menor}Kg. De ', end='')
for v in Pessoas:
    if v[1] == menor:
        print(f'{v[0]}.', end=' ')
print(f'O(s) maior(es) peso(s) é {maior}Kg. De ', end='')
for v in Pessoas:
    if v[1] == maior:
        print(f'{v[0]}.', end=' ')
print(f'{"FIM":=^40}')
