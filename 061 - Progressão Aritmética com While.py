print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
Termo = int(input('Digite o primeiro Termo da PA: '))
Razão = int(input('Digite a Razão da PA: '))
count = 1
while count < 11:
    print('{}º Termo: {}'.format(count, Termo))
    Termo += Razão
    count += 1
print('>>>>> FIM <<<<<')
