print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('=' * 40)
print(''' Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:
  
A)Quantas vezes o número 9 apareceu.
b)Em que posição foi digitado o número 3.
C)Quais foram os números pares.''')
print('=' * 40)
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print('ANÁLISE DE DADOS DA TUPLA')
print('-' * 40)
Números = (int(input('Digite o Primeiro Número: ')), int(input('Digite o Segundo Número: ')),
           int(input('Digite o Terceiro Número: ')), int(input('Digite o Quarto Número: ')))
print(f'Os números digitados foram: {Números}')
print(f'O número 9 apareceu {Números.count(9)} vezes.')
if Números.count(3) >= 1:
    print(f'O número 3 foi digitado pela primeira vez na posição: {Números.index(3) + 1}')
else:
    print('O número 3 não foi digitado.')
print('Veja os número(s) Par(es) digitados:')
for n in Números:
    if n % 2 == 0:
        print(n, end=' ')
print(' ')
print('=' * 40)
print(f'{"FIM":^40}')
