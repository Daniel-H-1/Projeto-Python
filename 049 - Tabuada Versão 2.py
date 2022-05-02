print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Refaça o Desafio 009, mostrando a tabuadda de um número
que o usuário escolher, só que agora utilizando um laço for.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
m = int(input('Digite um valor para fazermos a tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(m, c, m * c))
print('>>>>> FIM <<<<<')
