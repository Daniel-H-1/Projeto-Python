print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print('''Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre: 

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('ANALISANDO A LISTA')
print('-' * 40)
Lista = list()
while True:
    Lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja digitar outro número [S/N]: ')).strip()[0]
    while resposta not in 'SsNn':
        print('Resposta inválida...', end='')
        resposta = str(input('Deseja digitar outro número [S/N]: ')).strip()[0]
    if resposta in 'Nn':
        break
print(f'Foram digitados {len(Lista)} Números.')
Lista.sort(reverse=True)
print(f'A lista formada com os números digitados em ordem descrecente: {Lista}')
if Lista.count(5) > 0:
    print(f'O número 5 foi digitado {Lista.count(5)}')
else:
    print('O número cinco não foi digitado.')
print('-' * 40)
print(f'{"FIM":=^40}')
