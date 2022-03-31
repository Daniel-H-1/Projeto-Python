print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Faça um programa que leia um ano qualque e mostre se ele é ano BISSEXTO.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from datetime import date
Ano = int(input('Digite um ano, ou analise o ano atual apertando 0: '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print('O ano {} é bissexto'.format(Ano))
else:
    print('O ano {} não é um ano bissexto'.format(Ano))
print('>>>>> FIM <<<<<')
