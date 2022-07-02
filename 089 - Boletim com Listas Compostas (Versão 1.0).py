print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa que leia nome e duas notas de vários alunos. No final mostre o boletim tendo a média de cada
um e permita que o usuário possa mostrar as notas de cada aluno individualmente.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('BOLETIM DE NOTA')
print('-' * 40)
Boletim = list()
Aluno = []

while True:
    print(f'{"ALUNO":^40}')
    Aluno.append(str(input('Nome: ')))
    Aluno.append(float(input('Nota 1: ')))
    Aluno.append(float(input('Nota 2: ')))
    Aluno.append(float((Aluno[1] + Aluno[2]) / 2))
    Boletim.append(Aluno[:])
    Aluno.clear()
    decisão = str(input('Deseja cadastrar outro aluno? [S/N]: '))[0].upper()
    while decisão not in 'SN':
        print('RESPOSTA INVÁLIDA')
        decisão = str(input('Deseja cadastrar outro aluno? [S/N]: '))[0].upper()
    print('-' * 40)
    if decisão in 'N':
        break
print(f'{"ALUNOS":-^22}')
print(f'{"Num":<6}{"NOME":<12} {"MÉDIA":<5}')
for pos, valor in enumerate(Boletim):
    print(f'{pos + 1:<5} {valor[0]:<12} {valor[3]:.1f}')
while True:
    escolha = int(input('Você quer ver as notas de qual aluno? (999 para interromper) '))
    if escolha == 999:
        print('INTERROMPENDO...')
        break
    if escolha <= 0:
        print('Número Inválido!')
    elif escolha - 1 <= len(Boletim) - 1:
        print(f'As notas de {Boletim[escolha - 1][0]} são {Boletim[escolha - 1][1:3]}')
    else:
        print('Número não Encontrado!')
    print('-' * 40)
print(f'{"FIM":=^40}')
