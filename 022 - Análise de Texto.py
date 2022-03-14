print('             >>>>>> INSTRUÇÕES DO PROGRAMA <<<<<<   ')
print('''CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

1 - O nome com todas as letras maiúsculas
2 - O nome com todas as letras minúsculas.
3 - Quantas letras ao todo (sem considerar os espaços).
4 - Quantas letras tem o primeiro nome.''')

print(' ')
print('            >>>>>> RESOLUÇÃO DO PROGRAMA <<<<<<   ')

Nome_Completo = str(input('Digite o seu nome completo: ')).strip()
Espaços = Nome_Completo.count(' ')
Caracteres = len(Nome_Completo)
Nome_sem_espaço = Caracteres - Espaços
Primeiro_Nome = Nome_Completo.split()

print(' ')
print('Nome todo em letra Maiúscula: ', Nome_Completo.upper())
print('Nome todo em letra minúscula:', Nome_Completo.lower())
print('O seu nome possui {} Letras ao todo!'.format(Nome_sem_espaço))
#print('O seu nome possui {} Letras ao todo!'.format(len(Nome_Completo) - Nome_Completo.count(' ')))
print('O seu primeiro nome possui {} Letras!'.format(len(Primeiro_Nome[0])))
#print('O seu primeiro nome possui {} Letras!!'.format(Nome_Completo.find(' ')))

