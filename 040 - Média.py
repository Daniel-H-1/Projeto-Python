print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Escreva um programa que leia duas notas de um aluno, e calcule a média, \n'
      'mostrando uma mensagem no final, de acordo com a média atingida:\n'
      '- Média abaixo de 5.0: REPROVADO.\n'
      '- Média entre 5.0 e 6.9: RECUPERAAÇÃO.\n'
      '- Média entre 7.0 e 10.0: APROVADO.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
Nota1 = float(input('Digite a primeira nota: '))
Nota2 = float(input('Digite a sua segunda nota: '))
Média = (Nota1 + Nota2) / 2

if Média < 5.0:
      print('Sua média é {}, logo você foi Reprovado!!!'.format(Média))
elif Média < 7.0:
      print('Sua média é {}, Então você está em Recuperação!!!'.format(Média))
elif Média >= 7.0 and Média <= 10.0:
      print('Sua média é {}, Você está Aprovado!!!'.format(Média))
print('>>>>> FIM <<<<<')
