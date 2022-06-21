print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e
os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('DIVINDO OS PARES E ÍMPARES')
print('-' * 40)
Lista_Geral = list()
Lista_Par = list()
Lista_Ímpar = list()
while True:
    Lista_Geral.append(int(input('Digite um número: ')))
    resposta = str(input('Quer digitar outro número [S/N]: ')).strip()[0]
    while resposta not in 'SsNn':
        print('Digite uma resposta válida...', end='')
        resposta = str(input('Quer digitar outro número [S/N]: ')).strip()[0]
    if resposta in 'Nn':
        break
for posição, número in enumerate(Lista_Geral):
    if número % 2 == 0:
        Lista_Par.append(número)
    else:
        Lista_Ímpar.append(número)
print(f'Lista Geral: {Lista_Geral}')
print(f'Lista de Números Par: {Lista_Par}')
print(f'Lista de Números Ímpar: {Lista_Ímpar}')
print('-' * 40)
print(f'{"FIM":=^40}')
