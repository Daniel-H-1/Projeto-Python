print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: \n'
      'Se ele ainda vai se alistar ao serviço militar; \n'
      'Se é a hora de se alistar; \n'
      'Se já passou do tempo de alistamento. \n'
      'Seu programa também deverá calcular quanto tempo falta para se alistar, ou quanto tempo devia ter se alistado.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from datetime import date
nascimento = int(input('Digite o ano do seu nascimento:'))
atual = date.today().year
idade = atual - nascimento

print(' ')
print('Quem nasceu em {} possui {} anos em {}'.format(nascimento, idade, atual))

if idade < 18:
      saldo = 18 - idade
      print('Falta {} Anos para você se alistar!!'.format(saldo))
      ano = atual + saldo
      print('Você vai se alistar daqui a {} Anos'.format(ano))
elif idade == 18:
      print('Você deve se alistar imediatamente!!!')
elif idade > 18:
      atraso = idade - 18
      print('Você deveria ter se alistado a {} Anos.'.format(atraso))
      ano = atual - atraso
      print('Seu alistamento foi em {}.'.format(ano))
print('>>>>> FIM <<<<<')
