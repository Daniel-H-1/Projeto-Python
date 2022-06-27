print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Crie um programa onde o usuário possa digitar sete valores númericos e cadestre-os
em uma lista única que mantenha separados os valores pares e ímpares. 
No final mostre os valores pares e ímpares em ordem crescente.''')

print(' ')
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
print('Lista Composta com Pares e Ímpares')
print('-' * 40)
Lista = []
Pares = []
Ímpares = []
for intervalo in range(1, 8):
    n = int(input(f'Digite o {intervalo}º Valor: '))
    if n % 2 == 0:
        Pares.append(n)
        Pares.sort()
    else:
        Ímpares.append(n)
        Ímpares.sort()
Lista.append(Pares[:])
Lista.append(Ímpares[:])
Pares.clear()
Ímpares.clear()
print(f'Números Pares digitados: {Lista[0]}')
print(f'Números Ímpares digitados: {Lista[1]}')
print(f'{"FIM":=^40}')
