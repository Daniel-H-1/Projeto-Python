print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('A confederação Nacional de Natação precisa de um programa que leia o ano de nascimmento, \n'
      'de um atleta e mostre a sua categoria de acordo com a sua idade:\n'
      '- Até 9 anos: MIRIM.\n'
      '- Até 14 anos: INFANTIL.\n'
      '- Até 19 anos: JUNIOR.\n'
      '- Até 20 anos: SENIOR.\n'
      '- Acima de 20 anos: MASTER')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from datetime import date
print('Digite preencha as informações a seguir!')
nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(' ')
print('De acordo com o ano de nascimento você possui {} Anos, logo '.format(idade), end='')
if idade <= 9:
      print(' a sua  categoria em natação é MIRIM!!!')
elif idade <= 14:
      print('A sua categoria na natação é INFANTIL.')
elif idade <= 19:
      print('a sua categoria é JUNIOR.')
elif idade == 20:
      print('a sua categoria na natação é SENIOR. ')
elif idade >= 21:
      print('a sua categoria é MASTER.')
print('>>>>> FIM <<<<<')