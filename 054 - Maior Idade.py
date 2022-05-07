print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Crie um programa que leia o ano de nascimento de Sete Pessoas. No final
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from datetime import date
n = 1
atual = date.today().year
maiores = 0
menores = 0
print('Olá digite o ano de nascimento de sete pessoas a seguir: ')
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {} pessoa: '.format(n)))
    n += 1
    idade = atual - pessoa
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('Dentre o ano de nascimento das pessoas descritas: ')
print('{} são maiores de idade e {} são menores de idade.'.format(maiores, menores))
print('Considero a idade de 21 anos como maioridade!')
print('>>>>> FIM <<<<<')
