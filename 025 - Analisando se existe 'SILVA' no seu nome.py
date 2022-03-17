print('             >>>>>> INSTRUÇÕES DO PROGRAMA <<<<<<   ')
print('''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME"''')

print(' ')
print('            >>>>>> RESOLUÇÃO DO PROGRAMA <<<<<<   ')

Nome = str(input('Digite o seu nome: ')).strip()

print('Seu nome tem Silva? {}'.format('silva' in Nome.lower()))

#if ('Silva' or 'SILVA') in Nome:
    #print('O seu nome possui a palavra "Silva".')
#else:
    #print('O seu nome não possui a palavra "Silva".')