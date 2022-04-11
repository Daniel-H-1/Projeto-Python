print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma dessas mensagens: \n'
      'O primeiro valor é maior \n'
      'O segundo valor é maior \n'
      'Não existe valor maior, os dois são iguais')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
Num1 = int(input('Digite o primeiro número: '))
Num2 = int(input('Digite o segundo número: '))

if Num1 > Num2:
      print('O primeiro valor é maior')
elif Num2 > Num1:
      print('O segundo número é maior')
else:
      print('Os dois números são iguais!')
print('>>>>> FIM <<<<<')
