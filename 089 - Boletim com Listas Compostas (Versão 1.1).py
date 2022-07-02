print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa que leia nome e duas notas de vários alunos. No final mostre o boletim tendo a média de cada
um e permita que o usuário possa mostrar as notas de cada aluno individualmente.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('BOLETIM DE NOTA')
print('-' * 40)
Boletim = list()
while True:
    print(f'{"ALUNO":^40}')
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = float((nota1 + nota2) / 2)
    Boletim.append([nome, [nota1, nota2], média])
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
    print(f'{pos + 1:<5} {valor[0]:<12} {valor[2]:.2f}')
while True:
    escolha = int(input('Você quer ver as notas de qual aluno? (999 para interromper) '))
    if escolha == 999:
        print('INTERROMPENDO...')
        break
    elif escolha <= 0:
        print('Número Inválido!')
    elif escolha - 1 <= len(Boletim) - 1:
        print(f'As notas de {Boletim[escolha - 1][0]} são {Boletim[escolha - 1][1]}')
    else:
        print('Número não encontrado!')
    print('-' * 40)
print(f'{"FIM":=^40}')
