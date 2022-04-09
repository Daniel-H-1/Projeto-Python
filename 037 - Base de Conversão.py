print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão.\n'
      '1 - Para Binário \n'
      '2 - Para Octal \n'
      '3 - Para Hexadecimal')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
número = int(input('Digite um número: '))
binário = (bin(número) [2:])
octal = oct(número) [2:]
hexadecimal = hex(número) [2:]

print('Digite [1] se deseja converter para binário.')
print('Digite [2] se deseja converter para octal.')
print('Digite [3] se deseja converter para hexadecimal.')


Base = int(input('Digite a seguir: '))
if Base == 1:
      print(binário)
elif Base == 2:
      print(octal)
elif Base == 3:
      print(hexadecimal)
else:
      print('Você digitou um valor inválido!!!')
print('>>>>> FIM <<<<<')
