print('             >>>>>> INSTRUÇÕES DO PROGRAMA <<<<<<   ')
print('''CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE:

Exemplo: Ana Maria de Souza

O primeiro nome é: Ana
O último nome é: Souza
''')

print('            >>>>>> RESOLUÇÃO DO PROGRAMA <<<<<<   ')

nome_completo = str(input('Digite o seu nome Completo: '))
Primeiro = nome_completo.split()
#Último = nome_completo.rsplit()

print('O primeiro nome é:', Primeiro[0])
print('O último nome é: {}'.format(Primeiro[len(Primeiro)-1]))
#print('O último nome é: ', Primeiro.pop())
