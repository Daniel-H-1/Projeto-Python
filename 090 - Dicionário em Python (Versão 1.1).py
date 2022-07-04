print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('DICIONÁRIOS DE ALUNOS')
print('-' * 40)
Dicionário_Alunos = dict()
Alunos = list()
while True:
    Dicionário_Alunos['nome'] = str(input('Nome: ')).strip()
    Dicionário_Alunos['média'] = float(input('Média: '))
    if Dicionário_Alunos['média'] >= 7.0:
        Dicionário_Alunos['situação'] = str('Aprovado')
    elif Dicionário_Alunos['média'] >= 6.0:
        Dicionário_Alunos['situação'] = str('Recuperação')
    else:
        Dicionário_Alunos['situação'] = str('Reprovado')
    Alunos.append(Dicionário_Alunos.copy())
    resposta = str(input('Deseja cadastrar outro aluno? [S/N] '))
    while resposta not in 'SsNn':
        print('Resposta Inválida')
        resposta = str(input('Deseja cadastrar outro aluno? [S/N] '))
    if resposta in 'Nn':
        print('-' * 30)
        break
    print('-' * 30)
print(f'{"BOLETIM":^30}')
print('=' * 30)
print(f'{"Cod.":<5} {"NOME":<7} {"MÉDIA":<6} {"SITUAÇÃO":^12}')
for pos, valor in enumerate(Alunos):
    print(f'{pos:<5} {valor["nome"]:<7} {valor["média"]:<6} {valor["situação"]}')
print(f'{"FIM":^=40}')
