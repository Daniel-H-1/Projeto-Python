print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('DICIONÁRIOS DE ALUNOS')
print('-' * 40)
aluno = {}
aluno['nome'] = str(input('Nome: ')).strip()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >=7:
    aluno['situação'] = str('Aprovado')
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = str('Recuperação')
else:
    aluno['situação'] = str('Reprovado')
print(f'{"DADOS":-^40}')
for keys, values in aluno.items():
    print(f'{keys} é igual a {values}')
print(f'{"FIM":=^40}')
