print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um 
dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule a acrescente, além da idade, com quantos anos a pessoas vai se aposentar.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('CADASTRO DE PESSOA')
print('-' * 40)
from datetime import date
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano de Nascimento'] = int(input('Data de Nascimento: '))
ano_atual = date.today().year
#ano_atual = date.now().year
pessoa['idade'] = ano_atual - pessoa['Ano de Nascimento']
pessoa['Carteira de Trabalho'] = int(input('Carteira de Trabalho: '))
if pessoa['Carteira de Trabalho'] > 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Digite o salário: '))
    pessoa['Ano de Aposentadoria'] = pessoa['Ano de Contratação'] + 35
    pessoa['Idade de Aposentadoria'] = pessoa['idade'] + (pessoa['Ano de Aposentadoria'] - date.today().year)
    print(f'{pessoa["Nome"]} você vai se aposentar em {pessoa["Ano de Aposentadoria"]}')

print(f'{"DADOS DO DICIONÁRIO":-^40}')
for k, v in pessoa.items():
    print(f'    - {k} é {v}')
