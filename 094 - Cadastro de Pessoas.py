from typing import List, Any, Type

print(f'{" INSTRUÇÕES DO PROGRAMA ":=^40}')
print('''Crie um programa que leia o NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre: 

A) Quantas pessoas cadastradas.
B) A MÉDIA de idade das pessoas.
C) Uma lista com MULHERES.
D) Uma lista com IDADE acima da MÉDIA.''')


print(' ')
print(f'{" RESOLUÇÃO DO DESAFIO ":=^40}')

print(' CADASTRO DE PESSOAS')
print('-' * 40)
print('')

pessoas_cadastradas = []
cadastro_pessoa = dict()

while True:
    cadastro_pessoa['Nome'] = str(input('Digite o Nome: '))
    while True:
        cadastro_pessoa['Sexo'] = str(input('Digite o SEXO: ')).upper()[0]
        if cadastro_pessoa['Sexo'] in 'MF':
            break
        print ('ERRO! Por favor, digite apenas M ou F.')
    cadastro_pessoa['idade'] = int(input('Idade: '))
    pessoas_cadastradas.append(cadastro_pessoa.copy())
    while True:
        resposta = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resposta in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    print('-'*40)
    print('')
    if resposta == 'N':
        break

print(pessoas_cadastradas)

print(f'{" FIM ":=^40}')