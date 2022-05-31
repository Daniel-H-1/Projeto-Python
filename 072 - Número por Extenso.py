print(f'{"INSTRUÇÕES DO PROGRAMA":^40}')
print('''Crie um programa que tenha uma tupla totalmente
 preenchida com uma contagem por extenso, de ZERO até VINTE.
 
 Seu programa deverá ler um número pelo teclado(entre 0 e 20)
 e mostrá-lo por extenso.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":^40}')
print('=' * 40)
print(f'{"NÚMERO EXTENSO":^40}')
Tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
         'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    print('-' * 40)
    n = int(input('Digite um Número do 0 até 20: '))
    while n < 0 or n > 20:
        n = int(input('Digite um valor válido de 0 até 20: '))
    print(f'O número {n} por extenso é {Tupla[n]}.')
    resposta = str(input('Deseja ver outro número? [S/N] ')).strip().upper()[0]
    if resposta not in "S":
        break
print('=' * 40)
print(f'{"FIM":^40}')
